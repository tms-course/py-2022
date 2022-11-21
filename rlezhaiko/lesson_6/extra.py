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


def find_all_keys_in_dict(dictionary: dict, list_of_path: list = [], path: tuple = ()) -> list:
    """
    Find all keys in dict function.
    
    :param dictionary: the dictionary
    :param list_of_path: the list of paths
    :param path: path in tuple
    :returns: return list of paths
    """        
    for key, value in dictionary.items():
        key_path = path + (key,)
        list_of_path.append(key_path)
        if hasattr(value, 'items'):
            find_all_keys_in_dict(value, list_of_path, key_path)
    return list_of_path


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


def updating_dict(data: dict, paths: list, value: str) -> None:
    """
    Updating dict function.
    
    :param data: data in dict format
    :param paths: the list of path
    :param value: the value to add
    :returns: return None
    """
    for path in paths:
        if paths.index(path) == len(paths) - 1:
            data.update({path: int(value) if value.isdigit() else value.strip()})
        else:
            if not (path in data and hasattr(data[path], 'values')):
                data.update({path: {paths[paths.index(path) + 1]: 0}})
            data = data[path]


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
            list_tmp.append(line)
            list_tmp.append('')
    elif line[0] not in punctuation.replace('!', '', 1):
        type_of_command = 2
        if line.count('=') == 1:
            command, argument = line.split('=')
            command, argument = command.strip(), argument.strip()
            list_tmp.append(command)
            list_tmp.append(argument)
        else:
            type_of_command = 0 
            list_tmp.append('')
            list_tmp.append('')   
    
    
    if type_of_command:
        flag_valid = not (list_tmp[0] == 'exit' and len(list_tmp[1]) > 0) or (len(list_tmp[1]) >= 2)
    list_tmp.insert(0, flag_valid)
    list_tmp.insert(1, type_of_command)
    return list_tmp


def check_argument_for_valid(list_of_paths: list, argument: str) -> list:
    """
    Check argument for valid function.
    
    :param list_of_paths: the list of paths
    :param argument: the argument
    :returns: return list with path in tuple and True if argument in collection, False otherwise 
    """
    path_tuple, flag_valid_argument, list_tmp = (), False, []
    for path in list_of_paths:
        if argument in path:
            path_tuple = path
            flag_valid_argument = True
            break
    list_tmp.append(path_tuple)
    list_tmp.append(flag_valid_argument)
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
            list_of_paths = find_all_keys_in_dict(collection)
            path_tuple, flag_valid_argument = check_argument_for_valid(list_of_paths, argument)
            list_of_paths.clear()
            if flag_valid_argument:
                printing_element(list(path_tuple), collection)
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
        list_of_paths = find_all_keys_in_dict(collection)
        path_tuple, flag_valid_argument = check_argument_for_valid(list_of_paths, argument)
        list_of_paths.clear()
        if flag_valid_argument:
            delete_element(collection, list(path_tuple))
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
