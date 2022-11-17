"""
3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве
значений кортеж состоящий из 2-х элементов - имя(str), возраст(int). Сделать около 5-6 
элементов словаря. Записать данный словарь на диск в json-файл.
"""

from random import randint
import json

tuples_of_users = [(i, randint(10, 100)) for i in ['John', 'Silva', 'Kate', 'Sam', 'Adam', 'Julia']]
dict_of_users = {}.fromkeys([randint(100000, 999999) for _ in range(6)], None)
i = 0
for key, _ in dict_of_users.items():
    dict_of_users[key] = tuples_of_users[i]
    i += 1

with open('task_3_data.json', 'w') as f:
    json.dump(dict_of_users, f)