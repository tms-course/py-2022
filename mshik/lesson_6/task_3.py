"""
Задание 3.

Создат словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве
значений кортеж состоящий из 2-х элементов — имя(str), возраст(int).
Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл. 
"""
import json
from os.path import dirname, abspath


USERS = {
         "012345": ("Maxim", 17), 
         "123456": ("Jasy", 22), 
         "234567": ("Alex", 38), 
         "345678": ("Adam", 25),
         "456789": ("Yura", 23)
        }


with open(f"{abspath(dirname(__file__))}/data/users.json", "w") as output_file:
        json.dump(USERS, output_file)