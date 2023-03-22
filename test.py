import json
with open("config.json", "r+") as f:
    print(json.load(f)["callsign"])
    file = json.load(f)
    # file["callsign"] = "Athena"
    # json.dump(file)
    # print(json.load(f)["callsign"])