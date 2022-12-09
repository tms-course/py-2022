"""
Создать словарь, в качестве ключа которого будет 6-ти занчное число (id),
а в качестве значений - кортеж из двух элементов: имя(str) и возраст(int).
Сделать 5-6 элементов словаря. Записать данный словарь на диск в json-файл.
"""
import json

data_dct = {
    '123456': ('Maks', 27),
    '132435': ('Alex', 28),
    '213141': ('Pashu', 42),
    '312654': ('Andrew', 32),
    '112233': ('Inna', 25),
    '223311': ('Anna', 28)
    }
user_list = [{'id': personal_id, 'name': name, 'age': age} for personal_id, (name, age) in data_dct.items()]
with open('task_3.json', 'w') as f:
    json.dump(user_list, f, indent=3)
