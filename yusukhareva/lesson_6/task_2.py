"""
Создает файл, записывает сразу две строки, потом две оставшиеся добавляет
:param line: вводимая строка
:param first_input: массив строк для первичной записи в файл
:param second_input: массив строк для последующей записи в файл
:param f1: запись двух первых строк
:param f2: запись двух последних строк
"""

first_input = list()
n = int(input ('Количество строк при первом вводе:'))

for i in range(n):
    line = input("Введите строку " + str(i+1) + ": ")
    first_input.append(line + "\n")

with open ('textfile.txt','w') as f1:
    for line in first_input:
        f1.write(line)
f1.close()

second_input  = list()
n = int(input ('Количество строк при втором вводе:'))

for i in range(n):
    line = input("Введите строку " + str(i+1) + ": ")
    second_input.append(line + "\n")

with open ('textfile.txt','a') as f1:
    for line in second_input:
        f1.write(line)
f1.close()