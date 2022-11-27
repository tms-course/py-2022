"""
Создает файл, записывает сразу две строки, потом две оставшиеся добавляет
:param first_line: первая строка
:param second_line: вторая строка
:param thirt_line: третья строка
:param fourth_line: четвертая строка
:param f1: запись двух первых строк
:param f2: запись двух последних строк
"""
first_line = (input('Enter 1th line: '))
second_line = (input('Enter 2nd line: '))
thirt_line = (input('Enter 3rd line: '))
fourth_line = (input('Enter 4th line: '))

with open ('textfile.txt','w') as f1:
    f1.writelines(list(map(lambda x : x+'\n', [first_line, second_line])))
f1.close()

with open ('textfile.txt','a') as f2:
    f2.writelines(list(map(lambda x : x+'\n', [thirt_line, fourth_line])))
f2.close()