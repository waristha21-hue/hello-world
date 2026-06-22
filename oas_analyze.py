# -*- coding: utf-8 -*-
import json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

man = json.loads((Path(__file__).parent / "oas_download_manifest.json").read_text(encoding="utf-8"))

def item_no(folder):
    """เลขข้อของ segment ที่อยู่ใต้แบรนด์ (segment index 1)."""
    parts = folder.split("/")
    if len(parts) < 2:
        return None
    m = re.match(r'\s*(\d+)', parts[1])
    return int(m.group(1)) if m else None

total = len(man)
in_scope = [x for x in man if (n := item_no(x["folder"])) is not None and 1 <= n <= 10]

# per root: total vs in-scope(1-10)
roots = {}
for x in man:
    r = x["folder"].split("/")[0]
    roots.setdefault(r, {"total": 0, "scope": 0})
    roots[r]["total"] += 1
    n = item_no(x["folder"])
    if n is not None and 1 <= n <= 10:
        roots[r]["scope"] += 1

print(f"TOTAL files in manifest : {total}")
print(f"IN-SCOPE (item 1-10)    : {len(in_scope)}")
print(f"EXCLUDED                : {total - len(in_scope)}")
print()
print(f"{'ROOT FOLDER':45} {'total':>6} {'1-10':>6}")
print("-" * 60)
for r, v in sorted(roots.items(), key=lambda kv: -kv[1]["total"]):
    print(f"{r[:44]:45} {v['total']:>6} {v['scope']:>6}")
