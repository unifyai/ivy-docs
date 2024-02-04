# Take 2 arguments, a repo name and version. Add it to <repo-name>.json

import sys
import json
import os

REPO = sys.argv[1]
VERSION = sys.argv[2]
json_file = os.path.join(os.path.dirname(__file__), f"{REPO}.json")

with open(json_file, "r", encoding="utf8") as f:
    data = json.load(f)

data.append({
    "version": VERSION,
    "url": f"https://unify.ai/docs/{VERSION}/{REPO}/"
})

with open(json_file, "w", encoding="utf8") as f:
    json.dump(data, f)

print(f"Added {VERSION} to {REPO}.json")
