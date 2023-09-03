# Take 1 argument, a repo name. This script will create a default version file with dev
# version

import sys
import json
import os

REPO = sys.argv[1]
json_file = os.path.join(os.path.dirname(__file__), f"{REPO}.json")

data = [
    {
        "version": "dev",
        "url": f"https://unify.ai/docs/{REPO}/"
    }
]

with open(json_file, "w", encoding="utf8") as f:
    json.dump(data, f)

print(f"Added {REPO}.json")
