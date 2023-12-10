#!/usr/bin/env python3

import json
from pathlib import Path
import re
import shutil
import urllib.request as request

docs_url = "https://devdocs.io/docs.json"
doc_prefix_url = "https://documents.devdocs.io"

index_name = "index.json"
db_name = "db.json"
mtime_name = "mtime"

def download1(url, path, info):
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

def download2(path, name):
    path.mkdir(parents=True, exist_ok=True)

    index = download1(doc_prefix_url+"/"+name+"/"+index_name, path / index_name, name+" index")
    db = download1(doc_prefix_url+"/"+name+"/"+db_name, path / db_name, name+" db")

    return index, db

def clean(path):
    for child in path.iterdir():
        shutil.rmtree(child) if child.is_dir() else child.unlink()

def save_db(path, db):
    for file, content in db.items():
        file_path = doc_path / (file + ".html")
        file_path.parent.mkdir(parents=True, exist_ok=True)

        content = re.sub('((href=")(?!http)[^"#]+)', '\\1.html', content)
        file_path.write_text(content)

def save_index(path, index):
    index = [{"name": e["name"], "path": e["path"]} for e in index["entries"]]
    json.dump(index, path.open("w"))

####################
root = Path("html")
if not root.exists():
    raise RuntimeError("Must be run from within the root directory")

with open("update.conf") as file:
    active = [line.rstrip() for line in file]

opener = request.build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
request.install_opener(opener)

index_path = root / index_name
index = download1(docs_url, index_path, "Overall index")

for doc in index:
    doc_mtime = str(doc["mtime"])
    doc_slug = doc["slug"]
    doc_path = root / doc["type"] / doc_slug

    if not doc_slug in active: continue

    mtime_path = doc_path / mtime_name
    mtime = mtime_path.read_text() if mtime_path.exists() else ""

    if doc_mtime != mtime:
        doc_index, doc_db = download2(doc_path, doc_slug)

        clean(doc_path)

        save_db(doc_path, doc_db)
        save_index(doc_path / index_name, doc_index)

        mtime_path.write_text(doc_mtime)

print("DONE")
