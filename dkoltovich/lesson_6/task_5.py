"""
task 5:
Прочитать сохраненный csv-файл и сохранить данные в excel-файл, кроме возраста -
столбец с этими данными не нужен
"""

import csv

import openpyxl

with open('data.csv', 'r') as f:
    rows = list(csv.reader(f))

wb = openpyxl.Workbook()
active_sheet = wb.active
active_sheet.append([''] + ['Person {}'.format(i) for i in range(1, len(rows))])
id_row, name_row, phone_row = [], [], []
for row in rows:
    id_row.append(row[0])
    name_row.append(row[1])
    phone_row.append(row[3])

active_sheet.append(id_row)
active_sheet.append(name_row)
active_sheet.append(phone_row)
wb.save('data.xlsx')
wb.close()
