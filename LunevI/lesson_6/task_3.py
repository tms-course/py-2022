"""
Создать словарь, в качестве ключа которого будет 6-ти занчное число (id),
а в качестве значений - кортеж из двух элементов: имя(str) и возраст(int).
Сделать 5-6 элементов словаря. Записать данный словарь на диск в json-файл.
"""
import json

data = {
    '111111': ('Andrew', 30),
    '222222': ('Jack', 31),
    '333333': ('Chester', 32),
    '444444': ('Mike', 33),
    '555555': ('Mark', 34),
    '666666': ('Jason', 35)
}

users_list = [{'id': user_id, 'name': user_name, 'age': user_age} for user_id, (user_name, user_age) in data.items()]


with open('data.json', 'w') as f:
    json.dump(users_list, f, indent=3)
