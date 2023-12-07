#!/usr/bin/env python3

import json
from pathlib import Path
import urllib.request as request

def spin():
    while True:
        for c in "||//--\\\\": yield c
spinner = spin()

def reporthook(*args):
    print(next(spinner) + "\b", end="", flush=True)

def download(url, path, info):
    print(f"{info:.<40s} ", end="")
    request.urlretrieve(url, path, reporthook)
    print("OK")

root = Path("html")
if not root.exists():
    raise RuntimeError("Must be run from with the root directory")

opener = request.build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
request.install_opener(opener)

docs_name = "docs.json"
docs_path = root / docs_name
download("https://devdocs.io/docs.json", docs_path, f"Document index ({docs_name})")

for doc in json.load(docs_path.open()):
    doc_mtime = str(doc["mtime"])
    doc_slug = doc["slug"]
    doc_path = root / doc["type"] / doc_slug

    mtime_path = doc_path / "mtime"
    mtime = mtime_path.read_text() if mtime_path.exists() else ""

    if doc_mtime != mtime:
        doc_path.mkdir(parents=True, exist_ok=True)

        for doc_name in [ "index.json", "db.json" ]:
            download(f"https://documents.devdocs.io/{doc_slug}/{doc_name}", doc_path / doc_name, f"{doc_slug} ({doc_name})") 

        mtime_path.write_text(doc_mtime)

print("DONE")
