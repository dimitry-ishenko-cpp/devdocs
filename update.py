#!/usr/bin/env python3

import json
from pathlib import Path
import urllib.request as request

def download(url, path, info):
    def spin():
        while True:
            for c in "||//--\\\\": yield c
    spinner = spin()

    def reporthook(*args):
        print(next(spinner) + "\b", end="", flush=True)

    print(f"{info:.<40s} ", end="")
    request.urlretrieve(url, path, reporthook)
    print("OK")

    return json.load(open(path))

index_name = "index.json"
db_name = "db.json"
mtime_name = "mtime"

with open("update.conf") as file:
    active = [line.rstrip() for line in file]

root = Path("html")
if not root.exists():
    raise RuntimeError("Must be run from within the root directory")

opener = request.build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
request.install_opener(opener)

index = download("https://devdocs.io/docs.json", root / index_name, "Doc index")

for doc in index:
    doc_mtime = str(doc["mtime"])
    doc_slug = doc["slug"]
    doc_path = root / doc["type"] / doc_slug

    if not doc_slug in active: continue

    mtime_path = doc_path / mtime_name
    mtime = mtime_path.read_text() if mtime_path.exists() else ""

    if doc_mtime != mtime:
        doc_path.mkdir(parents=True, exist_ok=True)

        url = "https://documents.devdocs.io/" + doc_slug + "/"
        doc_index = download(url + index_name, doc_path / index_name, doc_slug + "/index")
        doc_db = download(url + db_name, doc_path / db_name, doc_slug + "/db")

        mtime_path.write_text(doc_mtime)

print("DONE")
