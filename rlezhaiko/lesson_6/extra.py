"""
Написать программу, которая дает возможность редактирования коллекции данных и их 
сохранения и загрузки в редактор. Программа должна уметь добавлять значение по ключу 
(даже вложенному), удалять значение, показывать состояние коллекции. Выбор структуры 
данных для хранения на ваше усмотрение.
"""

from sys import stdin
import os
from string import punctuation
import json
import argparse

parser = argparse.ArgumentParser(description='Save state collection editor')
parser.add_argument('-f', type=str, default='', help='Provide an str (default: "")')
arguments = parser.parse_args()

collection = {}
if arguments.f != '':
    if os.path.exists(arguments.f):
        with open(f'{arguments.f}', 'r') as f:
            collection.update(json.load(f))
    else:
        print('Данного файла не существует! Создана пустая коллекция.')


help_str = '''
!show - отображает коллекцию (!show * - отображет всю коллекцию, !show element - отображает element)
!del - удаляет элемент из коллекции (!del x    or     !del x.v.z)
x = 20 - создает либо обновляет элемент, поддерживает обращение по дереву объектов x.v.z
!help - Выводит описание функций
!exit - Выход из программы'''
print('Введите !help для просмотра функций.')


def printing_element(path: list, data: dict) -> None:
    """
    Printing element function.
    
    :param path: path
    :param data: collection in dict format
    :returns: return None
    """
    for element in path: 
        data = data[element]
    print(json.dumps(data, indent=4))


def updating_dict(data: dict, path: list, value: str) -> None:
    """
    Updating dict function.
    
    :param data: data in dict format
    :param path: the list of path
    :param value: the value to add
    :returns: return None
    """
    while len(path):
        key = path.pop(0)

        if key not in data:
            data[key] = data.get(key, {})
        else:
            data[key] = {} if len(path) else data.get(key)
    
        if len(path) == 0:
            data.update({key: int(value) if value.isdigit() else value.strip()})
        data = data[key]


def delete_element(data: dict, paths: list) -> None:
    """
    Delete element function.
    
    :param data: data in dict format
    :param paths: the list of path
    :returns: return None
    """
    if len(paths) == 1:
        del data[paths[0]]
    else:
        data = data[paths[0]]  
        paths.pop(0)
        delete_element(data, paths)


def check_valid_path(data: dict, key_to_find: list) -> bool:
    """
    Delete element function.
    
    :param data: data in dict format
    :param paths: the list of path
    :returns: return True if valid path, False otherwise
    """
    flag_valid = True
    while len(key_to_find):
        current_key = key_to_find.pop(0)
        if type(data) == dict:
            if current_key in data:
                data = data[current_key]
            else:
                flag_valid = False
                break
        else:
            flag_valid = False
            break
    return flag_valid


def parsing_command(line: str) -> list:
    """
    Parsing command and check line for valid value function.
    
    :param line: the line for parsing
    :returns: return list with True if right line, False otherwise, type_of_command, command, argument
    """
    list_tmp = []
    type_of_command, flag_valid = 0, False
    if line[0] == '!':
        type_of_command = 1
        line = line.replace('!', '', 1)
        if ' ' in line:
            list_tmp.extend(line.split())
        else:
            list_tmp.extend([line, ''])
    elif line[0] not in punctuation.replace('!', '', 1):
        type_of_command = 2
        if line.count('=') == 1:
            command, argument = line.split('=')
            command, argument = command.strip(), argument.strip()
            list_tmp.extend([command, argument])
        else:
            type_of_command = 0 
            list_tmp.extend(['', ''])  
    
    if type_of_command:
        flag_valid = not (list_tmp[0] == 'exit' and len(list_tmp[1]) > 0) or (len(list_tmp[1]) >= 2)
    list_tmp.insert(0, flag_valid)
    list_tmp.insert(1, type_of_command)
    return list_tmp



def run_command(command: str, argument: str) -> bool:
    """
    Run command function.
    
    :param command: command for programm
    :param argument: argument for command
    :returns: return bool
    """
    flag_exit = False
    if command == 'show':
        if argument == '*':
            print(json.dumps(collection, indent=4))
        else:    
            flag_valid_argument = check_valid_path(collection, argument.split('.'))
            if flag_valid_argument:
                printing_element(argument.split('.'), collection)
            else:
                print(f'Ключа "{argument}" нет в коллекции')
    elif command == 'save':
        dirpath, filename = os.path.split(argument)
        if dirpath == '':
            with open(filename, 'w') as f:
                json.dump(collection, f)
        else:
            os.makedirs(dirpath, exist_ok=True)
            with open(dirpath + '/' + filename, 'w') as f:
                json.dump(collection, f)
    elif command == 'del':
        flag_valid_argument = check_valid_path(collection, argument.split('.'))
        if flag_valid_argument:
            delete_element(collection, argument.split('.'))
        else:
            print(f'Ключа "{argument}" нет в коллекции')
    elif command == 'help':
        print(help_str)
    elif command == 'exit':
        flag_exit = True
    else:
        print('Такой комманды не существует. Введите !help для просмотра функций.')
    
    return flag_exit


for line in stdin:
    line = line.strip()
    valid, type_of_command, command, argument = parsing_command(line)
    if type_of_command == 1:
        if valid:
            if run_command(command, argument):
                break
        else:
            print('Такой комманды не существует. Введите !help для просмотра функций.')
    elif type_of_command == 2:
        path = command.split('.')
        updating_dict(collection, path, argument)
    else:
        print('Такой комманды не существует. Введите !help для просмотра функций.')
