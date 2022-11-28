import csv
import json
from random import randint


with open('data.json') as f:
    data = json.load(f)

number_phone = [f'375(44){randint(100, 999)}-{randint(10,99)}-{randint(10,99)}' for _ in range(5)]

with open('file_3.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'Name', 'Age', 'Phone'])

    i = 0
    for key, value in data.items():
        writer.writerow((key, value[0], value[1], number_phone[i]))
        i += 1

