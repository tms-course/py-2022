import csv
import json
from random import randint


with open('best_json.json') as f:
    file = json.load(f)

number_phone = [f'{randint(100, 999)}-{randint(10,99)}-{randint(10,99)}' for _ in range(6)]

with open('best_csv.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('id', 'Name', 'Age', 'Phone'))

    i = 0
    for key, value in file.items():
        writer.writerow((key, value[0], value[1], number_phone[i]))
        i += 1

