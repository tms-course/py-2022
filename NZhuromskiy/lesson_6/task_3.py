"""
task 3:
Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве значений кортеж состоящий из
2-х элементов - имя(str), возраст(int). Сделать около 5-6 элементов словаря.
Записать данный словарь на диск в json-файл.
"""

import json


dictionary_names = {
    '145634': ('Nikita', 23),
    '167456': ('Pasha', 25),
    '345689': ('Ira', 24),
    '267456': ('Zhenya', 23),
    '567432': ('Timur', 30),
    '256432': ('Sergey', 34)
}


list_of_person = [{'id': id_of_the_person, 'name': name_of_the_person, 'age': age_of_the_person}
                  for id_of_the_person, (name_of_the_person, age_of_the_person) in dictionary_names.items()]

with open('./additional_task_3.json', 'w') as file:
    json.dump(list_of_person, file, indent=2)
