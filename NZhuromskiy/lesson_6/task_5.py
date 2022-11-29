"""
5. ** Прочитать сохраненный csv-файл и сохранить данные в excel-файл, кроме возраста -
столбец с этими данными не нужен.
"""

import csv
import openpyxl

with open('additional_task_4.csv', 'r') as file:
    rows = list(csv.reader(file))

file_person = openpyxl.Workbook()
active_sheet = file_person.active
active_sheet.append([''] + ['Person {}'.format(i) for i in range(1, len(rows))])
row_with_id, row_with_names, row_with_phone_number = [], [], []

for row in rows:
    row_with_id.append(row[0])
    row_with_names.append(row[1])
    row_with_phone_number.append(row[3])

active_sheet.append(row_with_id)
active_sheet.append(row_with_names)
active_sheet.append(row_with_phone_number)

file_person.save('additional_task_5.xlsx')
file_person.close()
