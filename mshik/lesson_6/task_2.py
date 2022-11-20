"""
Задание 2.

Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
Создать файл и записать в него первые 2 строки и закрыть файл. 
Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
В итоговом файле должно быть 4 строки, каждая из которых должна начинаться с новой строки. 
"""
from os.path import abspath, dirname


FILE_PATH = f"{abspath(dirname(__file__))}/data/inputs.txt"


inputs = [input("Please enter a string: ") + "\n" for _ in range(4)]
# Write first 2 rows into inputs.txt file
with open(FILE_PATH, "w") as file:
    file.writelines(inputs[:2])

# Append 2 more rows into inputs.txt file
with open(FILE_PATH, "a") as file:
    file.writelines(inputs[2:])
