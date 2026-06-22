# -*- coding: utf-8 -*-
"""สำรวจเมนู/ส่วนอื่นของ OAS ด้วยบัญชี suchart (นอกเหนือ Sale Marketing)"""
import re, sys, urllib.parse, html as htmllib
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


def main():
    u, p = load_creds(".env_scan")
    s = requests.Session()
    s.post(f"{OAS_BASE}/login_action",
           data={"username": u, "password": p, "submit": ""}, timeout=60)

    # ลองเปิดหน้าเมนูหลักหลังล็อกอิน
    for page in ["", "condition_Menu", "index.php", "main.php", "home"]:
        url = f"{OAS_BASE}/{page}"
        try:
            r = s.get(url, timeout=60)
        except Exception as e:
            print(f"[{page or '/'}] ERROR {e}")
            continue
        print(f"\n===== PAGE: '{page or '/'}' (status {r.status_code}, len {len(r.text)}) =====")
        if r.status_code != 200:
            continue
        # ดึงลิงก์เมนูทั้งหมด (href ที่ไม่ใช่ asset)
        links = re.findall(r'<a[^>]+href="([^"#?][^"]*)"[^>]*>(.*?)</a>', r.text, re.DOTALL)
        seen = set()
        for href, text in links:
            t = re.sub(r"<[^>]+>", "", text)
            t = htmllib.unescape(re.sub(r"\s+", " ", t)).strip()
            if href.endswith((".css", ".js", ".png", ".jpg", ".ico", ".woff", ".woff2")):
                continue
            key = (href, t)
            if key in seen or not t:
                continue
            seen.add(key)
            print(f"   {t[:40]:42} -> {href[:80]}")


if __name__ == "__main__":
    main()
