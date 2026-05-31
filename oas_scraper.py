import requests, re, json, urllib.parse
from pathlib import Path

OAS_BASE = "http://183.89.246.93:2200"


def load_credentials():
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        print("ERROR: ไม่พบไฟล์ .env")
        return None, None
    creds = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip()
    return creds.get("OAS_USER"), creds.get("OAS_PASS")


def login(session, username, password):
    resp = session.post(
        f"{OAS_BASE}/login_action",
        data={"username": username, "password": password, "submit": ""},
        allow_redirects=True,
    )
    return "Welcome" in resp.text


def get_page(session, path=""):
    url = f"{OAS_BASE}/Doc_Sale.php?p={urllib.parse.quote(path)}"
    resp = session.get(url)
    return resp.text if resp.status_code == 200 else ""


def extract_items(html):
    folders = []
    files = []
    # Folder links: ?p=FolderName (without &del= or &copy=)
    for m in re.finditer(r'<a[^>]*href="\?p=([^"&]+)"[^>]*>', html):
        name = urllib.parse.unquote_plus(m.group(1))
        if name and name != "." and name not in folders:
            folders.append(name)
    # File download links
    for m in re.finditer(r'href="\?p=([^"&]+\.[a-zA-Z0-9]+)"', html):
        fname = urllib.parse.unquote_plus(m.group(1))
        if fname not in files:
            files.append(fname)
    # Separate actual folders from files in the folder list
    real_folders = [f for f in folders if "." not in f.split("/")[-1]]
    real_files = [f for f in folders if "." in f.split("/")[-1]] + files
    return real_folders, list(set(real_files))


def main():
    username, password = load_credentials()
    if not username:
        return

    session = requests.Session()
    print(f"Logging in...")

    if not login(session, username, password):
        print("ERROR: Login failed")
        return
    print("Login OK!\n")

    # Get root folders
    html = get_page(session)
    folders, _ = extract_items(html)

    print(f"=== Sale Marketing Data — {len(folders)} โฟลเดอร์ ===")
    for i, f in enumerate(folders, 1):
        print(f"  {i:2}. {f}")

    # Explore each folder
    print(f"\n=== สำรวจแต่ละโฟลเดอร์ ===")
    structure = {}
    for folder in folders:
        sub_html = get_page(session, folder)
        sub_folders, sub_files = extract_items(sub_html)
        structure[folder] = {"subfolders": sub_folders, "files": sub_files}
        total = len(sub_folders) + len(sub_files)
        print(f"  {folder}: {len(sub_folders)} folders, {len(sub_files)} files")

    # Save
    out_path = Path(__file__).parent / "oas_structure.json"
    out_path.write_text(json.dumps(structure, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nบันทึกไว้ที่: {out_path}")
    print("Done!")


if __name__ == "__main__":
    main()
