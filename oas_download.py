# -*- coding: utf-8 -*-
"""Recursively download ALL files from OAS (Tiny File Manager) to E:\\diskdisk.

Phase 1: crawl every folder, build a manifest of files.
Phase 2: download each file, preserving the OAS folder structure, skipping
files already present with a matching size (so it is safe to re-run / resume).
"""
import re, json, time, sys, threading, urllib.parse, html as htmllib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from requests.adapters import HTTPAdapter

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

OAS_BASE = "http://183.89.246.93:2200"
DEST = Path(r"E:\diskdisk")
MANIFEST = Path(__file__).parent / "oas_download_manifest.json"
LOG = Path(__file__).parent / "oas_download.log"

WORKERS = 6          # โหลดขนานกี่เส้น
SCOPE_MIN, SCOPE_MAX = 1, 10   # เอาเฉพาะข้อ 1-10 (เครื่อง/น้ำยา)
EXCLUDE_ROOTS = {"Nova Biomedical"}   # โฟลเดอร์ที่ไม่เอาเลย (Job ไม่ใช้)

INVALID = '<>:"|?*'
_lock = threading.Lock()


def item_no(folder):
    """เลขข้อของโฟลเดอร์ใต้แบรนด์ (segment ที่ 2) เช่น 'Sysmex CBC/2.Price List' -> 2"""
    parts = folder.split("/")
    if len(parts) < 2:
        return None
    m = re.match(r"\s*(\d+)", parts[1])
    return int(m.group(1)) if m else None


def in_scope(folder):
    if folder.split("/")[0] in EXCLUDE_ROOTS:
        return False
    n = item_no(folder)
    return n is not None and SCOPE_MIN <= n <= SCOPE_MAX

# ไฟล์วิดีโอ — ไม่ต้องดาวน์โหลด (ตามคำขอ)
VIDEO_EXT = {
    ".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".mpeg", ".mpg",
    ".webm", ".m4v", ".3gp", ".ts", ".vob", ".ogv", ".m2ts", ".mts", ".rmvb",
}


def is_video(name):
    return Path(name).suffix.lower() in VIDEO_EXT


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    with _lock:
        print(line, flush=True)
        with LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def load_credentials():
    creds = {}
    for line in (Path(__file__).parent / ".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip()
    return creds.get("OAS_USER"), creds.get("OAS_PASS")


def login(session, u, p):
    r = session.post(f"{OAS_BASE}/login_action",
                     data={"username": u, "password": p, "submit": ""},
                     allow_redirects=True, timeout=60)
    return "Welcome" in r.text or "Logout" in r.text


def get_page(session, path):
    url = f"{OAS_BASE}/Doc_Sale.php?p={urllib.parse.quote(path)}"
    r = session.get(url, timeout=60)
    return r.text if r.status_code == 200 else ""


def parse_listing(html, current_path):
    """Return (subfolders, files) for a folder page.
    subfolders: list of full relative paths
    files: list of filenames (in current_path)
    """
    subfolders, files = [], []

    # Folder links: href="?p=PATH"><i class="fa fa-folder-o">  (exclude .. go-back)
    for m in re.finditer(r'href="\?p=([^"&]+)"[^>]*>\s*<i class="fa fa-folder-o"', html):
        p = urllib.parse.unquote_plus(htmllib.unescape(m.group(1)))
        if p and p != current_path and p not in subfolders:
            subfolders.append(p)

    # Download links: title="Download" href="?p=PARENT&amp;dl=FILENAME"
    for m in re.finditer(r'title="Download"\s+href="\?p=[^"&]+&(?:amp;)?dl=([^"]+)"', html):
        fname = urllib.parse.unquote_plus(htmllib.unescape(m.group(1)))
        if fname and fname not in files:
            files.append(fname)

    return subfolders, files


def crawl(session, root_folders):
    manifest = []  # list of {"folder": relpath, "name": filename}
    stack = list(root_folders)
    visited = set()
    while stack:
        path = stack.pop(0)
        if path in visited:
            continue
        visited.add(path)
        html = get_page(session, path)
        if not html:
            log(f"WARN empty page: {path}")
            continue
        subs, files = parse_listing(html, path)
        for f in files:
            manifest.append({"folder": path, "name": f})
        # queue subfolders not yet visited
        for s in subs:
            if s not in visited:
                stack.append(s)
        log(f"crawled: {path}  (+{len(files)} files, +{len(subs)} folders) | queue {len(stack)}")
    return manifest


def get_root_folders(session):
    html = get_page(session, "")
    subs, _ = parse_listing(html, "")
    return subs


def safe_part(name):
    out = "".join("_" if c in INVALID else c for c in name).rstrip(" .")
    return out or "_"


def local_path(folder, name):
    parts = [safe_part(p) for p in folder.split("/")] + [safe_part(name)]
    return DEST.joinpath(*parts)


def download_file(session, folder, name, dest_path):
    url = f"{OAS_BASE}/Doc_Sale.php?p={urllib.parse.quote(folder)}&dl={urllib.parse.quote(name)}"
    with session.get(url, stream=True, timeout=300) as r:
        if r.status_code != 200:
            return False, f"HTTP {r.status_code}"
        remote_len = r.headers.get("Content-Length")
        # skip if already downloaded with same size
        if dest_path.exists() and remote_len and dest_path.stat().st_size == int(remote_len):
            return True, "skip(same-size)"
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest_path.with_suffix(dest_path.suffix + ".part")
        size = 0
        with tmp.open("wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 16):
                if chunk:
                    f.write(chunk)
                    size += len(chunk)
        tmp.replace(dest_path)
        return True, f"{size:,} B"


def build_session():
    s = requests.Session()
    adapter = HTTPAdapter(pool_connections=WORKERS, pool_maxsize=WORKERS * 2, max_retries=2)
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    return s


def main():
    LOG.write_text("", encoding="utf-8")
    u, p = load_credentials()
    s = build_session()
    if not login(s, u, p):
        log("LOGIN FAILED")
        return
    log("LOGIN OK")
    DEST.mkdir(parents=True, exist_ok=True)

    # Phase 1: ใช้ manifest เดิมถ้ามี (ประหยัดเวลา crawl) ไม่งั้น crawl ใหม่
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        log(f"reuse manifest: {len(manifest)} files")
    else:
        roots = get_root_folders(s)
        log(f"root folders: {len(roots)}")
        manifest = crawl(s, roots)
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"=== MANIFEST: {len(manifest)} files ===")

    # กรอง: เฉพาะข้อ 1-10 + ไม่ใช่วิดีโอ
    work = [x for x in manifest if in_scope(x["folder"]) and not is_video(x["name"])]
    excluded = len(manifest) - len(work)
    log(f"=== SCOPE: item {SCOPE_MIN}-{SCOPE_MAX}, non-video | download {len(work)} / excluded {excluded} ===")

    counters = {"ok": 0, "skip": 0, "fail": 0}
    n = len(work)

    def task(item):
        dest = local_path(item["folder"], item["name"])
        try:
            success, info = download_file(s, item["folder"], item["name"], dest)
            with _lock:
                if success and info.startswith("skip"):
                    counters["skip"] += 1
                elif success:
                    counters["ok"] += 1
                else:
                    counters["fail"] += 1
            return success, info, item
        except Exception as e:
            with _lock:
                counters["fail"] += 1
            return False, f"ERROR {e}", item

    done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = [ex.submit(task, it) for it in work]
        for fut in as_completed(futures):
            success, info, item = fut.result()
            done += 1
            if not success:
                log(f"FAIL [{done}/{n}] {item['folder']}/{item['name']} -> {info}")
            elif not info.startswith("skip") or done % 50 == 0:
                log(f"[{done}/{n}] ok={counters['ok']} skip={counters['skip']} | {item['name']} -> {info}")

    log(f"=== DONE: downloaded {counters['ok']}, skipped {counters['skip']}, failed {counters['fail']}, scope-total {n} ===")


if __name__ == "__main__":
    main()
