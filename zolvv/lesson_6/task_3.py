"""
task_3
Создать словарь в качестве ключа которого будет 6ти значное число (id), а в качестве
значений кортеж состоящий из 2-х элементов - имя(str), возраст(int). Сделать 6
элементов словаря. Записать данный словарь на диск в json-файл.
"""

import json
data = {
    '000001': ('John', 41),
    '000002': ('Ralf', 22),
    '000003': ('Emma', 48),
    '000004': ('Natasha', 39),
    '000005': ('Elena', 19),
    '000006': ('Anna', 25)
}
list_of_people = [{'id': personal_id,
                   'name': name,
                   'age': age
                   } for personal_id, (name, age) in data.items()
                  ]
with open('./data.json', 'w') as f:
    json.dump(list_of_people, f, indent=4)
