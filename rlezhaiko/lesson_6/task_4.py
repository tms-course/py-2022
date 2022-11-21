"""
4. Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой
которого озаглавив каждый столбец и добавив новый столбец "телефон".
"""

from random import randint
import json
import csv

list_of_users = []
with open('task_3_data.json', 'r') as f:
    list_of_users = json.load(f)

rows = [['id', 'name', 'age', 'phone']]
phone_numbers = [str(randint(100, 999)) + '-' + str(randint(0, 99)) + '-' + str(randint(0, 99)) for _ in range(len(list_of_users))]
for user in list_of_users:
    list_tmp = list(user.values())
    list_tmp.append(phone_numbers[list_of_users.index(user)])
    rows.append(list_tmp)

with open('task_4_data.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerows(rows)