#!/usr/bin/env python3

import json
from pathlib import Path
from urllib.request import build_opener, install_opener, Request, urlopen, urlretrieve

def download(url, path, info):
    def spin():
        while True:
            for c in "||//--\\\\": yield c
    spinner = spin()

    def reporthook(*args):
        print(next(spinner) + "\b", end="", flush=True)

    print(f"{info:.<40s} ", end="")
    urlretrieve(url, path, reporthook)
    print("OK")

with open("update.conf") as file:
    active = [line.rstrip() for line in file]

root = Path("html")
if not root.exists():
    raise RuntimeError("Must be run from within the root directory")

opener = build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
install_opener(opener)

req = Request("https://devdocs.io/docs.json", headers={"User-agent": "Mozilla/5.0"})
index = json.load(urlopen(req))

for doc in index:
    doc_mtime = str(doc["mtime"])
    doc_slug = doc["slug"]
    doc_path = root / doc["type"] / doc_slug

    if not doc_slug in active: continue

    mtime_path = doc_path / "mtime"
    mtime = mtime_path.read_text() if mtime_path.exists() else ""

    if doc_mtime != mtime:
        doc_path.mkdir(parents=True, exist_ok=True)

        for doc_name in [ "index.json", "db.json" ]:
            download(f"https://documents.devdocs.io/{doc_slug}/{doc_name}", doc_path / doc_name, f"{doc_slug} ({doc_name})")

        mtime_path.write_text(doc_mtime)
