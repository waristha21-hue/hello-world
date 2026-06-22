# -*- coding: utf-8 -*-
"""สแกนโครงสร้าง OAS ด้วยบัญชีอื่น (อ่านอย่างเดียว ยังไม่โหลดไฟล์)
เทียบ root folders กับ oas_structure.json เดิม (บัญชี Waristha)
"""
import re, json, sys, urllib.parse, html as htmllib
from pathlib import Path
import requests

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OAS_BASE = "http://183.89.246.93:2200"
HERE = Path(__file__).parent


def load_creds(fname):
    creds = {}
    for line in (HERE / fname).read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip()
    return creds.get("OAS_USER"), creds.get("OAS_PASS")


def login(s, u, p):
    r = s.post(f"{OAS_BASE}/login_action",
               data={"username": u, "password": p, "submit": ""},
               allow_redirects=True, timeout=60)
    return ("Welcome" in r.text or "Logout" in r.text), r


def get_page(s, path):
    r = s.get(f"{OAS_BASE}/Doc_Sale.php?p={urllib.parse.quote(path)}", timeout=60)
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


def main():
    u, p = load_creds(".env_scan")
    s = requests.Session()
    ok, r = login(s, u, p)
    print(f"LOGIN as '{u}': {'OK' if ok else 'FAILED'} (status {r.status_code})")
    if not ok:
        print("  -> ตรวจ username/password อีกครั้ง หรือบัญชีอาจถูกล็อก")
        return

    # root folders + immediate subfolder / file counts
    html = get_page(s, "")
    roots, root_files = parse_listing(html, "")
    print(f"\nบัญชีนี้เห็น root folders: {len(roots)} | ไฟล์ที่ root: {len(root_files)}\n")
    struct = {}
    print(f"{'ROOT FOLDER':45} {'subfolders':>10} {'files':>6}")
    print("-" * 65)
    for f in roots:
        sub_html = get_page(s, f)
        subs, files = parse_listing(sub_html, f)
        struct[f] = {"subfolders": subs, "files": files}
        print(f"{f[:44]:45} {len(subs):>10} {len(files):>6}")

    (HERE / "oas_structure_suchart.json").write_text(
        json.dumps(struct, ensure_ascii=False, indent=2), encoding="utf-8")

    # compare roots vs old account
    old_path = HERE / "oas_structure.json"
    if old_path.exists():
        old_roots = set(json.loads(old_path.read_text(encoding="utf-8")).keys())
        new_roots = set(roots)
        only_new = sorted(new_roots - old_roots)
        only_old = sorted(old_roots - new_roots)
        print("\n=== เทียบกับบัญชีเดิม (Waristha) ===")
        print(f"เหมือนกัน: {len(new_roots & old_roots)} โฟลเดอร์")
        print(f"เฉพาะบัญชีนี้ (suchart) เห็นเพิ่ม: {only_new if only_new else 'ไม่มี'}")
        print(f"บัญชีเดิมเห็นแต่บัญชีนี้ไม่เห็น: {only_old if only_old else 'ไม่มี'}")

    print("\nบันทึกโครงสร้างไว้ที่ oas_structure_suchart.json")


if __name__ == "__main__":
    main()
