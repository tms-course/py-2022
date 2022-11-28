"""
4. Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой которого озаглавив
каждый столбец и добавив новый столбец "телефон".
"""

import json
import csv
import random
from random import randint


code_for_number = [29, 33, 44]

with open('./additional_task_3.json', 'r') as file:
    data = json.load(file)

for person in data:
    person['phone'] = f"+375 ({random.choice(code_for_number)}) {randint(111, 999)}-{randint(11, 99)}-{randint(11, 99)}"

with open('./additional_task_4.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age', 'phone'])
    for person in data:
        writer.writerow([*person.values()])
