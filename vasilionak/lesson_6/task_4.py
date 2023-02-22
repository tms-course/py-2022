"""
Прочитать сохраненный json-файл и записать данные на диск csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"
"""

import csv
import json
from random import randint


with open('data.json') as f:
    data = json.load(f)

def gen_phone():
    return f'{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}'

with open('file_3.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'Name', 'Age', 'phone'])
    for obj in data:
        writer.writerow([*obj.values(), gen_phone()])


    


