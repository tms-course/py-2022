"""
task 2:
Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать файл
и записать в него первые 2 строки и закрыть файл. Затем открыть файл на редактирование
и дозаписать оставшиеся 2 строки. В итоговом файле должны быть 4 строки,
каждая из которых должна начинаться с новой строки.
"""

first_string = input('Enter first string: ')
second_string = input('Enter second string: ')
third_string = input('Enter third string: ')
fourth_string = input('Enter fourth string: ')

with open('./file.txt', 'w') as f:
    f.writelines([first_string + '\n', second_string + '\n'])

with open('./file.txt', 'a') as f:
    f.writelines([third_string + '\n', fourth_string + '\n'])


