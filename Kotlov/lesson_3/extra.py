spisok = []

while True:
    print('\$', end=' ')
    vvod = input()
    command, *data = vvod.split()
    new_data = ' '.join(data).replace(',', ' ').split()

    if command == 'add':
        spisok.extend(new_data)
    elif command == 'view':
        print(spisok)
    elif command == 'rm':
        for i in new_data:
            if i in spisok:
                spisok.remove(i)
            else:
                print(f'Элемента "{i}" нет в коллекции!!!')
    elif command == 'clr':
        spisok = []
    elif command == 'exit':
        break
