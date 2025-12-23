# json_csv.py
# Basic usage of json and csv modules

import json
import csv

# JSON example
data = {
    "name": "Pito",
    "role": "student",
    "active": True
}

json_string = json.dumps(data, indent=2)
print("JSON output:")
print(json_string)

# CSV example
rows = [
    ["name", "age"],
    ["Pito", 21],
    ["Alex", 25]
]

print("\nCSV output:")
for row in rows:
    print(",".join(map(str, row)))
