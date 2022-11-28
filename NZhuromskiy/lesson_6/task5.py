import csv
import openpyxl

rows = []
with open('additional_task_4.csv', 'r') as f:
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