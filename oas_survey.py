# -*- coding: utf-8 -*-
"""สำรวจไฟล์ใน Contract + Condition BKD (ยังไม่โหลด) — สรุปรายแบรนด์ + รายชื่อไฟล์
เขียนผลลง oas_survey.txt ให้ Job เปิดอ่าน
"""
import re, json, sys, urllib.parse, html as htmllib
from pathlib import Path
import requests

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OAS_BASE = "http://183.89.246.93:2200"
HERE = Path(__file__).parent
OUT = HERE / "oas_survey.txt"
EXCLUDE_ROOTS = {"Nova Biomedical"}

SECTIONS = [
    ("Doc_Contract", "Contract", "oas_manifest_Contract.json"),
    ("Doc_msale_bkd", "Condition BKD", "oas_manifest_ConditionBKD.json"),
]
lines = []


def out(s=""):
    print(s, flush=True)
    lines.append(s)


def load_creds():
    c = {}
    for line in (HERE / ".env_scan").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            c[k.strip()] = v.strip()
    return c.get("OAS_USER"), c.get("OAS_PASS")


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
        if path in visited or path.split("/")[0] in EXCLUDE_ROOTS:
            continue
        visited.add(path)
        h = get_page(s, page, path)
        if not h:
            continue
        subs, files = parse_listing(h, path)
        for f in files:
            manifest.append({"folder": path, "name": f})
        for sub in subs:
            if sub not in visited:
                stack.append(sub)
    return manifest


def survey(manifest, label):
    out("=" * 70)
    out(f"  {label}  —  รวม {len(manifest)} ไฟล์")
    out("=" * 70)
    # group by brand (root segment)
    brands = {}
    for x in manifest:
        b = x["folder"].split("/")[0]
        brands.setdefault(b, []).append(x)
    # summary table
    out(f"\n  {'แบรนด์':28} {'ไฟล์':>6}")
    out("  " + "-" * 40)
    for b in sorted(brands, key=lambda k: -len(brands[k])):
        out(f"  {b[:27]:28} {len(brands[b]):>6}")
    # detail: file names per brand
    out("\n  --- รายชื่อไฟล์ (ย่อ subfolder) ---")
    for b in sorted(brands):
        out(f"\n  ▶ {b}  ({len(brands[b])} ไฟล์)")
        for x in brands[b]:
            sub = "/".join(x["folder"].split("/")[1:])
            prefix = f"[{sub}] " if sub else ""
            out(f"      {prefix}{x['name']}")
    out("")


def main():
    u, p = load_creds()
    s = requests.Session()
    s.post(f"{OAS_BASE}/login_action",
           data={"username": u, "password": p, "submit": ""}, timeout=60)

    for page, label, mf in SECTIONS:
        path = HERE / mf
        if path.exists():
            manifest = json.loads(path.read_text(encoding="utf-8"))
        else:
            manifest = crawl(s, page)
            path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        survey(manifest, label)

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n>>> บันทึกรายการเต็มไว้ที่ {OUT}")


if __name__ == "__main__":
    main()
