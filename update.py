#!/usr/bin/env python3

import json
from pathlib import Path
import re
import shutil
from tempfile import TemporaryDirectory as tempdir
import urllib.request as request

def download(url, banner):
    def spin():
        while True:
            for c in "||//--\\\\": yield c
    spinner = spin()

    def reporthook(*args):
        print(next(spinner) + "\b", end="", flush=True)

    with tempdir() as dirname:
        path = Path(dirname) / "file.json"

        print(f"{banner:.<40s} ", end="")
        request.urlretrieve(url, path, reporthook)
        with open(path) as fp: content = json.load(fp)
        print("OK")

    return content

def purge(path):
    if path.exists():
        for child in path.iterdir():
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    else: path.mkdir()

def save_db(path, db):
    for item, content in db.items():
        item_path = path / (item + ".html")
        item_path.parent.mkdir(parents=True, exist_ok=True)

        content = re.sub('((href=")(?!http)[^"#]+)', '\\1.html', content)
        item_path.write_text(content)

def save_index(path, index):
    index_path = path / "index.json"
    index = { e["name"]: (e["path"] + ".html") for e in index["entries"] }
    with open(index_path, "w") as fp: json.dump(index, fp)

####################
docs_url = "https://devdocs.io/docs.json"
doc_templ_url = "https://documents.devdocs.io/{}/{}"

root_path = Path.cwd()
html_path = root_path / "html"
dl_path   = root_path / "download.conf"

with open(dl_path) as fp:
    dl_doc = [ ln.rstrip() for ln in fp ]
    dl_all = len(dl_doc) == 1 and dl_doc[0] == "*"

opener = request.build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
request.install_opener(opener)

docs = download(docs_url, "Document index")
for doc in docs:
    name = doc["slug"]
    path = html_path / name

    if dl_all or name in dl_doc:
        mtime_path = path / "mtime"
        old_mtime = mtime_path.read_text() if mtime_path.exists() else ""

        mtime = str(doc["mtime"])
        if mtime != old_mtime:
            index = download(doc_templ_url.format(name, "index.json"), name + "-index")
            db = download(doc_templ_url.format(name, "db.json"), name + "-db")

            purge(path)
            save_db(path, db)
            save_index(path, index)

            mtime_path.write_text(mtime)

print("DONE")
