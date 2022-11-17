"""
4. Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой
которого озаглавив каждый столбец и добавив новый столбец "телефон".
"""

from random import randint
import json
import csv

dict_of_users = {}
with open('task_3_data.json', 'r') as f:
    dict_of_users = json.load(f)

with open('task_4_data.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')
    rows, headers = [], ['id', 'name', 'age', 'phone']
    rows.append(headers) 
    keys, values = list(dict_of_users.keys()), list(dict_of_users.values()) 
    phone_numbers = [str(randint(100, 999)) + '-' + str(randint(0, 99)) + '-' + str(randint(0, 99)) for _ in range(len(keys))]
    
    for element in values:
        element.insert(0, keys[values.index(element)])
        element.append(phone_numbers[values.index(element)])
    
    rows += values
    csv_writer.writerows(rows)