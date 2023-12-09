#!/usr/bin/env python3

import json
from urllib.request import Request, urlopen

req = Request("https://devdocs.io/docs.json", headers={"User-agent": "Mozilla/5.0"})
index = json.load(urlopen(req))

for doc in index: print(doc["slug"])
