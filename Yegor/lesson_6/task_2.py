""""
Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
Создать файл и записать в него первые 2 строки и закрыть файл.
Открыть файл на редактирование и дозаписать оставшиеся 2 строки.
В итоговом файле должно быть 4 строки, каждая из которых начинается с новой строки.
"""
lines = list(input("Введите строку: ") + '\n' for i in range(4))


with open('task_2.txt', 'w') as f:
    f.writelines(lines[:2])

with open('task_2.txt', 'a') as f:
    f.writelines(lines[2:])
