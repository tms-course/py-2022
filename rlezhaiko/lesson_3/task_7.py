import sys

collection = []
help_str = '''add - Добавляет элемент/элементы в коллекцию (add 5, 7,   10)
view - Выводит коллекцию на экран
rm - Удаляет элемент/элементы из коллекции (rm 5, 7,   10)
help - Выводит описание функций
quit - Выход из программы'''
print('Введите help для просмотра функций.')

for line in sys.stdin:
    words_of_line = line.replace(',', ' ').split()
    command, *elements = words_of_line

    if command == 'add':
        collection.extend(elements)   
    elif command == 'view':
        print(collection)
    elif command == 'rm':
        for element in elements:
            if element in collection:
                collection.remove(element)
            else:
                print(f'Элемента {element} нет в коллекции.')
    elif command == 'help': 
        print(help_str)
    elif command == 'quit':
        print('Выход из программы.')
        break
    else:
        print('Такой комманды не существует. Введите help для просмотра функций.')