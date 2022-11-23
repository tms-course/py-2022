import json
from random import randint

list_id = [randint(1_000_00, 9_999_99) for _ in range(6)]

dict_data = {i: (input("name: "), int(input("age: "))) for i in list_id}

with open('best_json.json', 'w') as f:
    json.dump(dict_data, f, indent=5)
