"""
Создать словарь, в качестве ключа которого будет 6-ти занчное число (id),
а в качестве значений - кортеж из двух элементов: имя(str) и возраст(int).
Сделать 5-6 элементов словаря. Записать данный словарь на диск в json-файл.
"""
import json

data_dict = {
        '111111': ('Wick', 36),
        '222222': ('Sara', 42),
        '333333': ('Liam', 24),
        '444444': ('Tom', 31),
        '555555': ('Kate', 33)
    }

list_of_data = [{'id': user_id, 'name': user_name, 'age': user_age}
for user_id, (user_name, user_age) in data_dict.items()]

with open('data.json', 'w') as f:
   json.dump(data_dict, f)



