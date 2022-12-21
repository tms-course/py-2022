import json
import csv
from random import randint

with open('data.json') as f:
    data = json.load(f)

print(data)

def gen_phone():
    return f'{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}'

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age', 'phone'])
    for obj in data:
        writer.writerow([*obj.values(), gen_phone()])
