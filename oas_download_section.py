# -*- coding: utf-8 -*-
"""ดาวน์โหลดคลังไฟล์ OAS ส่วนอื่น (Contract, Condition BKD) ด้วยบัญชี suchart.
เก็บแยกโฟลเดอร์ ไม่ปนกับ Sale Marketing | parallel + skip video + resume.
"""
import re, json, time, sys, threading, urllib.parse, html as htmllib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from requests.adapters import HTTPAdapter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OAS_BASE = "http://183.89.246.93:2200"
HERE = Path(__file__).parent
CREDS = ".env_scan"            # บัญชี suchart
WORKERS = 6
INVALID = '<>:"|?*'
EXCLUDE_ROOTS = {"Nova Biomedical"}
VIDEO_EXT = {".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".mpeg", ".mpg",
             ".webm", ".m4v", ".3gp", ".ts", ".vob", ".ogv", ".m2ts", ".mts", ".rmvb"}

# (เมนู page, โฟลเดอร์ปลายทาง, ไฟล์ manifest, ไฟล์ log)
JOBS = [
    ("Doc_Contract",   Path(r"E:\diskdisk\_Contract"),     "oas_manifest_Contract.json"),
    ("Doc_msale_bkd",  Path(r"E:\diskdisk\_Condition_BKD"), "oas_manifest_ConditionBKD.json"),
]
LOG = HERE / "oas_section.log"
_lock = threading.Lock()


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    with _lock:
        print(line, flush=True)
        with LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def load_creds():
    c = {}
    for line in (HERE / CREDS).read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            c[k.strip()] = v.strip()
    return c.get("OAS_USER"), c.get("OAS_PASS")


def build_session():
    s = requests.Session()
    ad = HTTPAdapter(pool_connections=WORKERS, pool_maxsize=WORKERS * 2, max_retries=2)
    s.mount("http://", ad)
    return s


def login(s, u, p):
    r = s.post(f"{OAS_BASE}/login_action",
               data={"username": u, "password": p, "submit": ""}, timeout=60)
    return "Welcome" in r.text or "Logout" in r.text


def is_video(name):
    return Path(name).suffix.lower() in VIDEO_EXT


def safe_part(name):
    return ("".join("_" if c in INVALID else c for c in name).rstrip(" .")) or "_"


def get_page(s, page, path):
    r = s.get(f"{OAS_BASE}/{page}.php?p={urllib.parse.quote(path)}", timeout=60)
    return r.text if r.status_code == 200 else ""


def parse_listing(html, cur):
    subs, files = [], []
    for m in re.finditer(r'href="\?p=([^"&]+)"[^>]*>\s*<i class="fa fa-folder-o"', html):
        p = urllib.parse.unquote_plus(htmllib.unescape(m.group(1)))
        if p and p != cur and p not in subs:
            subs.append(p)
    for m in re.finditer(r'title="Download"\s+href="\?p=[^"&]+&(?:amp;)?dl=([^"]+)"', html):
        fn = urllib.parse.unquote_plus(htmllib.unescape(m.group(1)))
        if fn and fn not in files:
            files.append(fn)
    return subs, files


def crawl(s, page):
    html = get_page(s, page, "")
    roots, _ = parse_listing(html, "")
    roots = [r for r in roots if r not in EXCLUDE_ROOTS]
    manifest, stack, visited = [], list(roots), set()
    while stack:
        path = stack.pop(0)
        if path in visited:
            continue
        visited.add(path)
        if path.split("/")[0] in EXCLUDE_ROOTS:
            continue
        h = get_page(s, page, path)
        if not h:
            continue
        subs, files = parse_listing(h, path)
        for f in files:
            manifest.append({"folder": path, "name": f})
        for sub in subs:
            if sub not in visited:
                stack.append(sub)
        log(f"  crawl [{page}] {path} (+{len(files)}f, +{len(subs)}d) | queue {len(stack)}")
    return manifest


def download_file(s, page, folder, name, dest):
    url = f"{OAS_BASE}/{page}.php?p={urllib.parse.quote(folder)}&dl={urllib.parse.quote(name)}"
    with s.get(url, stream=True, timeout=300) as r:
        if r.status_code != 200:
            return False, f"HTTP {r.status_code}"
        rlen = r.headers.get("Content-Length")
        if dest.exists() and rlen and dest.stat().st_size == int(rlen):
            return True, "skip"
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_suffix(dest.suffix + ".part")
        size = 0
        with tmp.open("wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 16):
                if chunk:
                    f.write(chunk)
                    size += len(chunk)
        tmp.replace(dest)
        return True, f"{size:,} B"


def run_job(s, page, dest_root, manifest_file):
    log(f"=== SECTION {page} -> {dest_root} ===")
    mf = HERE / manifest_file
    if mf.exists():
        manifest = json.loads(mf.read_text(encoding="utf-8"))
        log(f"reuse manifest {manifest_file}: {len(manifest)} files")
    else:
        manifest = crawl(s, page)
        mf.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"manifest {manifest_file}: {len(manifest)} files")

    work = [x for x in manifest if not is_video(x["name"])]
    log(f"download {len(work)} files (skip {len(manifest)-len(work)} videos)")
    cnt = {"ok": 0, "skip": 0, "fail": 0}
    n = len(work)

    def task(item):
        parts = [safe_part(p) for p in item["folder"].split("/")] + [safe_part(item["name"])]
        dest = dest_root.joinpath(*parts)
        try:
            ok, info = download_file(s, page, item["folder"], item["name"], dest)
            with _lock:
                cnt["skip" if (ok and info == "skip") else ("ok" if ok else "fail")] += 1
            return ok, info, item
        except Exception as e:
            with _lock:
                cnt["fail"] += 1
            return False, f"ERROR {e}", item

    done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = [ex.submit(task, it) for it in work]
        for fut in as_completed(futs):
            ok, info, item = fut.result()
            done += 1
            if not ok:
                log(f"FAIL [{done}/{n}] {item['folder']}/{item['name']} -> {info}")
            elif info != "skip" or done % 50 == 0:
                log(f"[{done}/{n}] ok={cnt['ok']} skip={cnt['skip']} | {item['name']} -> {info}")
    log(f"=== {page} DONE: ok {cnt['ok']}, skip {cnt['skip']}, fail {cnt['fail']}, total {n} ===")


def main():
    LOG.write_text("", encoding="utf-8")
    u, p = load_creds()
    s = build_session()
    if not login(s, u, p):
        log("LOGIN FAILED")
        return
    log(f"LOGIN OK as {u}")
    for page, dest_root, mf in JOBS:
        run_job(s, page, dest_root, mf)
    log("=== ALL SECTIONS DONE ===")


if __name__ == "__main__":
    main()
