"""
3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве
значений кортеж состоящий из 2-х элементов - имя(str), возраст(int). Сделать около 5-6 
элементов словаря. Записать данный словарь на диск в json-файл.
"""

from random import randint
import json

dict_of_users = {randint(100000, 999999): (i, randint(10, 100)) for i in ['John', 'Silva', 'Kate', 'Sam', 'Adam', 'Julia']}
list_of_users = [{'id': identificator, 'name': name, 'age': age} for identificator, (name, age) in dict_of_users.items()]

with open('task_3_data.json', 'w') as f:
    json.dump(list_of_users, f)