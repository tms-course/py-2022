"""
Прочитать сохраненный json-файл и записать данные на диск csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"
"""
import json
import csv
from random import randint

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

generate_phone_number = lambda: f"{randint(200, 999)}-{randint(10, 99)}-{randint(10, 99)}"

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["id", "name", "age", "phone"])

    for person in data:
        csv_writer.writerow([*person.values(), generate_phone_number()])
