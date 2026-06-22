import requests, urllib.parse
from pathlib import Path

OAS_BASE = "http://183.89.246.93:2200"

def load_credentials():
    creds = {}
    for line in (Path(__file__).parent / ".env").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip()
    return creds.get("OAS_USER"), creds.get("OAS_PASS")

def main():
    u, p = load_credentials()
    s = requests.Session()
    r = s.post(f"{OAS_BASE}/login_action", data={"username": u, "password": p, "submit": ""}, allow_redirects=True)
    print("LOGIN:", "Welcome" in r.text, "| status", r.status_code)

    # Probe a deep path: Sysmex CBC/2.Price List
    for path in ["Sysmex CBC/2.Price List", "Randox/2. Price List"]:
        url = f"{OAS_BASE}/Doc_Sale.php?p={urllib.parse.quote(path)}"
        resp = s.get(url)
        print("\n" + "="*60)
        print("PATH:", path, "| status", resp.status_code, "| len", len(resp.text))
        # Print raw HTML around anchors to learn link patterns
        html = resp.text
        # Show all <a href= occurrences
        import re
        anchors = re.findall(r'<a[^>]+href="[^"]*"[^>]*>.*?</a>', html, re.DOTALL)
        print(f"anchors found: {len(anchors)}")
        for a in anchors[:40]:
            print("  ", a.strip()[:200].replace("\n", " "))

if __name__ == "__main__":
    main()
