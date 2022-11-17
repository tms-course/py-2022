"""
Написать программу, которая дает возможность редактирования коллекции данных и их 
сохранения и загрузки в редактор. Программа должна уметь добавлять значение по ключу 
(даже вложенному), удалять значение, показывать состояние коллекции. Выбор структуры 
данных для хранения на ваше усмотрение.
"""

from sys import stdin
from string import punctuation

help_str = '''
!help - Выводит описание функций
!exit - Выход из программы'''
print('Введите !help для просмотра функций.')


def get_and_check_commands(string: str) -> list:
    words = string.replace('!', '', 1).split()
    if len(words) == 2:
        return list(words[0], words[1], True)
    else:
        return list(None, None, False)


for line in stdin:
    line = line.strip()
    if line[0] == '!':
        command, argument, valid = get_and_check_commands(line)
        if valid:
            pass
        
    elif line[0] in punctuation.replace('!', ''):
        print('Такой комманды не существует. Введите !help для просмотра функций.')
    print(line)