"""
Прочитать сохраненный json-файл и записать данные на диск csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"
"""

import csv
import json
from random import randint


with open('data.json') as f:
    data = json.load(f)


with open('file_3.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'Name', 'Age', 'Phone'])

    

    for key, value in data.items():
        
        writer.writerow(key, value[0], value[1], value[2])
        value[2].items = [f'375(44){randint(100, 999)}-{randint(10,99)}-{randint(10,99)}']

