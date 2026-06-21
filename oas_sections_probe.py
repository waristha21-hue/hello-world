# -*- coding: utf-8 -*-
"""สแกน root ของแต่ละส่วน Doc_* ด้วยบัญชี suchart — ดูว่าเข้าได้ไหม + มีอะไรบ้าง"""
import re, sys, urllib.parse, html as htmllib
from pathlib import Path
import requests

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OAS_BASE = "http://183.89.246.93:2200"
HERE = Path(__file__).parent

SECTIONS = {
    "Sale Marketing": "Doc_Sale",
    "Personal Data": "Doc_Personal",
    "Workgroup Data": "Doc_Workgroup",
    "Support Team": "Doc_Support",
    "Condition BKD": "Doc_msale_bkd",
    "Contract": "Doc_Contract",
}


def load_creds(fname):
    creds = {}
    for line in (HERE / fname).read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip()
    return creds.get("OAS_USER"), creds.get("OAS_PASS")


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


def main():
    u, p = load_creds(".env_scan")
    s = requests.Session()
    s.post(f"{OAS_BASE}/login_action",
           data={"username": u, "password": p, "submit": ""}, timeout=60)

    for label, page in SECTIONS.items():
        url = f"{OAS_BASE}/{page}.php?p="
        try:
            r = s.get(url, timeout=60)
        except Exception as e:
            print(f"\n### {label} ({page}.php): ERROR {e}")
            continue
        html = r.text
        # ตรวจว่าเข้าได้จริง (ไม่ใช่ redirect ไป login / ไม่มีสิทธิ์)
        denied = ("login" in r.url.lower()) or ("Permission" in html) or ("ไม่มีสิทธิ" in html)
        subs, files = parse_listing(html, "")
        status = "DENIED/redirect" if denied else "OK"
        print(f"\n### {label}  ({page}.php)  [{status}] status={r.status_code} len={len(html)}")
        if subs or files:
            print(f"    root: {len(subs)} folders, {len(files)} files")
            for f in subs[:30]:
                print(f"      [D] {f}")
            for f in files[:15]:
                print(f"      [F] {f}")
        else:
            print("    (ไม่พบโฟลเดอร์/ไฟล์ — อาจว่าง หรือเข้าไม่ได้)")


if __name__ == "__main__":
    main()
