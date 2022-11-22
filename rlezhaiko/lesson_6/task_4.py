"""
4. Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой
которого озаглавив каждый столбец и добавив новый столбец "телефон".
"""

from random import randint
import json
import csv

list_of_users, rows = [], [['id', 'name', 'age', 'phone']]
with open('task_3_data.json', 'r') as f:
    list_of_users = json.load(f)

gen_phone_num = lambda: str(randint(100, 999)) + '-' + str(randint(0, 99)) + '-' + str(randint(0, 99))
for user in list_of_users:
    rows.append([*user.values(), gen_phone_num()])

with open('task_4_data.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerows(rows)