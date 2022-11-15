collection = []
input_line = input()
while input_line != 'quit':
    if input_line == 'view':
        print(collection)
        input_line = input()
        continue

    action = input_line[0: input_line.find(' ')]
    input_line = input_line.removeprefix(action)
    list_of_arguments = input_line.replace(' ', '').split(',')
    if action == 'add':
        for argument in list_of_arguments:
            collection.append(int(argument) if argument.isdigit() else argument)
    else:
        for item in list_of_arguments:
            if collection.count(item) == 0:
                print(f'Элемента "{item}" нет в коллекции')
            else:
                collection.remove(item)

    input_line = input()

