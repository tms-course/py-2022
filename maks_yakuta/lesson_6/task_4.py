"""
Прочитать сохраненный json-файл и записать данные на диск в csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"
"""

import json
import csv
from random import randint
phone_number = lambda: f"{randint(100, 777)}-{randint(10, 99)}-{randint(10, 99)}"
with open('task_3.json', 'r') as f:
    data = json.load(f)

with open('task_4.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'Age', 'Phone'])
    for person in data:
        writer.writerow([*person.values(), phone_number()])


