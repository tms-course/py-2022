"""
3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве
значений кортеж состоящий из 2-х элементов - имя(str), возраст(int). Сделать около 5-6 
элементов словаря. Записать данный словарь на диск в json-файл.
"""

from random import randint
keys = [randint(100000, 999999) for _ in range(6)]
print(keys)
names = ['John', 'Silva', 'Sam', 'Kate', 'Rick', 'Morty']
values = [(names[i], randint(1, 100)) for i in range(6)]
print(values)
dict_users = {}.fromkeys(keys, ())
i = 0
for key, _ in dict_users.items():
    dict_users[key] = values[i]
    i += 1
print(dict_users)