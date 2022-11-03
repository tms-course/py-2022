import sys

collection = []
commands = ['add', 'view', 'rm', 'help', 'quit']
help_str = '''add - Добавляет элемент/элементы в коллекцию (add 5, 7,   10)\n
view - Выводит коллекцию на экран\n
rm - Удаляет элемент/элементы из коллекции (rm 5, 7,   10)\n
help - Выводит описание функций\n
quit - Выход из программы'''
print(f'Введите {commands[3]} для просмотра функций.')

for line in sys.stdin:
    words_of_line = line.strip(' ')
    if commands[0] in words_of_line and commands[1] not in words_of_line and commands[2] not in words_of_line and commands[3] not in words_of_line and commands[4] not in words_of_line:
        line = line.replace(' ', '')
        data_str = line[3:].strip()
        if ',' in data_str:
            elements = data_str.split(',')
            for element in elements:
                if element.isdigit():
                    collection.append(int(element))
                elif element.isdecimal():
                    collection.append(float(element))
                elif element == '':
                    continue
                else:
                    collection.append(element)
        else:
            if len(data_str) > 0 and data_str.isdigit():
                collection.append(int(data_str))
            elif len(data_str) > 0 and data_str.isdecimal():
                collection.append(float(data_str))
            elif len(data_str) > 0:
                collection.append(data_str)
            else:
                print('Вы ввели комманду без элементов!')   
    elif commands[1] in words_of_line and commands[0] not in words_of_line and commands[2] not in words_of_line and commands[3] not in words_of_line and commands[4] not in words_of_line:
        print(collection)
    elif commands[2] in words_of_line  and commands[1] not in words_of_line and commands[0] not in words_of_line and commands[3] not in words_of_line and commands[4] not in words_of_line:
        line = line.replace(' ', '')
        data_str = line[2:].strip()
        if ',' in data_str:
            elements = data_str.split(',')
            for element in elements:
                if element.isdigit() and int(element) in collection:
                    collection.remove(int(element))
                elif element.isdigit() and int(element) not in collection:
                    print(f'Элемента {element} нет в коллекции.')
                elif element.isdecimal() and float(element) in collection:
                    collection.remove(float(element))
                elif element.isdecimal() and float(element) not in collection:
                    print(f'Элемента {element} нет в коллекции.')
                elif element == '':
                    continue
                elif element in collection:
                    collection.remove(element)
                elif element not in collection:
                    print(f'Элемента {element} нет в коллекции.')
        else:
            if len(data_str) > 0:
                if data_str.isdigit() and int(data_str) in collection:
                    collection.remove(int(data_str))
                elif data_str.isdigit() and int(data_str) not in collection:
                    print(f'Элемента {data_str} нет в коллекции.')
                elif data_str.isdecimal() and float(data_str) in collection:
                    collection.remove(float(data_str))
                elif data_str.isdecimal() and float(data_str) not in collection:
                    print(f'Элемента {data_str} нет в коллекции.')
                elif data_str in collection:
                    collection.remove(data_str)
                elif data_str not in collection:
                    print(f'Элемента {data_str} нет в коллекции.')
            else:
                print('Вы ввели комманду без элементов!') 
    elif commands[3] in words_of_line  and commands[1] not in words_of_line and commands[2] not in words_of_line and commands[0] not in words_of_line and commands[4] not in words_of_line: 
        print(help_str)
    elif commands[4] in words_of_line  and commands[1] not in words_of_line and commands[2] not in words_of_line and commands[3] not in words_of_line and commands[0] not in words_of_line:
        print('Выход из программы.')
        break
    else:
        print(f'Такой комманды не существует. Введите {commands[3]} для просмотра функций.')