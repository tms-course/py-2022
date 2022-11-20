"""
task 4:
Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой
которого озаглавив каждый столбец и добавив новый столбец "телефон".
"""

import csv
import json
import random


with open('./data.json', 'r') as f:
    data = json.load(f)

gen_phone_number = lambda: str(random.randint(100, 999)) + '-' + str(random.randint(0, 99)) \
                           + '-' + str(random.randint(0, 99))

updated_data = {ID: (*data[ID], gen_phone_number()) for ID in data.keys()}
with open('./data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age', 'phone'])
    for key, value in updated_data.items():
        writer.writerow([key, *value])
