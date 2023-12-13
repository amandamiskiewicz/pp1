import json
with open("data.json") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key} : {value}")
