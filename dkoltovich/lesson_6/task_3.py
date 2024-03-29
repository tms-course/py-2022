"""
task 3:
Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве
значений кортеж состоящий из 2-х элементов - имя(str), возраст(int). Сделать около 5-6
элементов словаря. Записать данный словарь на диск в json-файл.
"""

import json
data = {
    '000001': ('John', 56),
    '000002': ('Leonel', 35),
    '000003': ('Leonardo', 45),
    '000004': ('Virgil', 29),
    '000005': ('Mike', 15),
    '000006': ('Anna', 22)
}
list_of_people = [{'id': personal_id,
                   'name': name,
                   'age': age
                   } for personal_id, (name, age) in data.items()
                  ]
with open('./data.json', 'w') as f:
    json.dump(list_of_people, f, indent=4)


