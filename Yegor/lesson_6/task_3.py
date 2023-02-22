"""
Создать словарь, в качестве ключа которого будет 6-ти занчное число (id),
а в качестве значений - кортеж из двух элементов: имя(str) и возраст(int).
Сделать 5-6 элементов словаря. Записать данный словарь на диск в json-файл.
"""
import json

data = {
    '012345': ('Alex', 10),
    '123456': ('Egor', 20),
    '234567': ('Cristiano', 30),
    '345678': ('Fill', 40),
    '456789': ('Carl', 50),
    '567890': ('Jphn', 60)
}

list_of_dict = [{'id': id, 'name': name, 'age': age} for id, (name, age) in data.items()]


with open('./task_3.json', 'w') as f:
    json.dump(list_of_dict, f, indent=4)
