"""
2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать файл и записать в него первые 2 строки
и закрыть файл. Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.В итоговом файле
должны быть 4 строки,каждая из которых должна начинаться с новой строки.
"""

user_input = [input("Введите строку {}: ".format(i + 1)) + '\n' for i in range(4)]

with open('./additional_task_2.txt', 'w') as file:
    file.writelines(user_input[:2])

with open('./additional_task_2.txt', 'a') as file:
    file.writelines(user_input[2:])