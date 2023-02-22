while True:
    name = input('Введите имя: ')
    age = int(input('Сколько Вам лет? '))
    
    if age <= 0:
        print('Ошибка, повторите ввод')
    elif age > 0 and age < 10:
        print(f'Привет, шкет {name}')
    elif age >= 10 and age <= 18:
        print(f'Как жизнь {name}?')
    elif age > 18 and age < 100:
        print(f'Чего желаете {name}?')
    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')