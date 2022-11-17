"""
5. *Прочитать сохраненный csv-файл и сохранить данные в excel-файл, кроме возраста -
столбец с этими данными не нужен. Таблица должна выглядеть, как на примере:
----------------------------------------
       | Person 1 | Person 2 | Person 3
----------------------------------------
id     | 111111   | 222043   | 679432
----------------------------------------
name   |   Sam    |   Adam   |   Jasy
----------------------------------------
phone  | 097-32-88| 090-45-41| 094-66-22
----------------------------------------
"""

import csv
import openpyxl

rows = []
with open('task_4_data.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        rows.append(row)

workbook = openpyxl.Workbook()
active_sheet = workbook.active
active_sheet.append(['' if i == 0 else f'Person {i}' for i in range(len(rows))])
for i in range(len(rows[0])):
    if i != 2:
        list_tmp = []
        for element in rows:
            list_tmp.append(element[i])
        active_sheet.append(list_tmp)

workbook.save('task_5_data.xlsx')
workbook.close()