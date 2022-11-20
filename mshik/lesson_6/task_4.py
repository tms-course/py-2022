"""
Задание 4.

Прочитать сохраненный json-файл и записать данные на диск в csv-файл, 
первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"
"""
import csv
import json
from random import randint
from os.path import dirname, abspath


DATA_DIR = f"{abspath(dirname(__file__))}/data/"


with open(DATA_DIR + "users.json", "r") as json_file:
    users = json.load(json_file)

# Added random number to each user
for user in users:
    user["phone"] = f"+375(44){randint(1111111, 9999999)}"

with open(DATA_DIR + "users.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["id", "name", "age", "phone"])
    for user in users:
        csv_writer.writerow(user.values())