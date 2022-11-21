while True:
    name = input('Введите имя: ')
    age = int(input("Возраст: "))

    if age <= 0 or str(age).isalpha():
        print('Ошибка, повторите ввод\n')
    elif 0 < age < 10:
        print(f'Привет, шкет {name}\n')
    elif 10 <= age <= 18:
        print(f'Как жизнь {name}?\n')
    elif 18 < age < 100:
        print(f'Что желаете {name}?\n')
    else:
        print(f'{name}, вы лжёте - в наше время столько не живут...\n')
