"""
Написать программу, которая дает возможность редактирования коллекции данных и их 
сохранения и загрузки в редактор. Программа должна уметь добавлять значение по ключу 
(даже вложенному), удалять значение, показывать состояние коллекции. Выбор структуры 
данных для хранения на ваше усмотрение.
"""

from sys import stdin
from string import punctuation
import json

help_str = '''
!show - отображает коллекцию (!show * - отображет всю коллекцию, !show element - отображает element)
!help - Выводит описание функций
!exit - Выход из программы'''
collection = {'x': {'c': 10}, 'z': 1}
print('Введите !help для просмотра функций.')


def find_dict_keys_with_recursion(dictionary: dict, list_of_paths: list = [], path: tuple = ()) -> list:
    """
    Find dict key with recursion function.
    
    :param dictionary: the dictionary
    :param list_of_paths: the list of paths
    :param path: path in tuple
    :returns: return list of paths
    """        
    for key, value in dictionary.items():
        key_path = path + (key,)
        list_of_paths.append(key_path)
        if hasattr(value, 'items'):
            find_dict_keys_with_recursion(value, list_of_paths, key_path)
    return list_of_paths


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


def parsing_command(line: str) -> list:
    """
    Parsing command and check line for valid value function.
    
    :param line: the line for parsing
    :returns: return list
    """
    list_for_return = []
    if ' ' in line:
        list_for_return.extend(line.split())
    else:
        command, argument = line, ''
        list_for_return.append(command)
        list_for_return.append(argument)
    flag_valid = bool('False' if (list_for_return[0] == 'exit' and len(list_for_return[1]) > 0) or (len(list_for_return[1]) >= 2) else 'True')
    list_for_return.insert(0, flag_valid)
    return list_for_return


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
            list_of_paths = find_dict_keys_with_recursion(collection)
            path = list(filter(lambda x: argument in x, list_of_paths))
            if len(path) == 1:
                printing_element(list(path[0]), collection)
            else:
                print(f'Ключа "{argument}" нет в коллекции')
    elif command == 'save':
        with open(f'{argument}', 'w') as f:
            json.dump(collection, f)
    elif command == 'help':
        print(help_str)
    elif command == 'exit':
        flag_exit = True
    else:
        print('Такой комманды не существует. Введите !help для просмотра функций.')
    
    return flag_exit


for line in stdin:
    line = line.strip()
    if line[0] == '!':
        valid, command, argument = parsing_command(line.replace('!', '', 1))
        if valid:
            if run_command(command, argument):
                break
        else:
            print('Такой комманды не существует. Введите !help для просмотра функций.')
    elif line[0] in punctuation.replace('!', ''):
        print('Такой комманды не существует. Введите !help для просмотра функций.')
    else:
        pass