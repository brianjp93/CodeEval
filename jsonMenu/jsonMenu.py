import sys
import json

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        total = 0
        if line == "":
            pass
        else:
            jsondict = json.loads(line)
            for item in jsondict["menu"]["items"]:
                if item != None and "label" in item:
                    total += item["id"]
            print(total)