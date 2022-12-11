"""
4. Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой которого озаглавив
каждый столбец и добавив новый столбец "телефон"
"""
import json
import csv
import random


with open('./task_3.json', 'r') as f:
    data = json.load(f)


phone_code = [17, 29, 33, 44]
phone_number = lambda: f"80 ({random.choice(phone_code)}){random.randint(111, 999)}-{random.randint(11, 99)}-{random.randint(11, 99)}"

with open('./task_4.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age', 'phone'])
    for human in data:
        writer.writerow([*human.values(), phone_number()])

