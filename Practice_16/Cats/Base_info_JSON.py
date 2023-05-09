import json

with open(f'D:\SF\Pet_House.txt', 'r', encoding="utf8") as f:
    pet_inf = json.load(f)

print(json.dumps(pet_inf, indent=4))