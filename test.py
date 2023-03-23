import json
file = {}
with open("config.json", "r") as f:
    file = json.load(f)

with open("config.json", "w") as f:
    file["callsign"] = "Athena"
    json.dump(file, f, indent=4)
    print(file)