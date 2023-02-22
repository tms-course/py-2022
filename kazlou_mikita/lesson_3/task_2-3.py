while True:
    name = input ('Введите ваше имя :')
    age = int(input ('Введите ваш возраст :'))

    if age <= 0:
        print('Ошибка, повторите ввод') 
    elif 0 < age < 10:
        print(f'Привет, шкет {name}!')
    elif 10 <= age <= 18:
        print(f'Как жизнь, {name}?')
    elif 18 < age < 100:
        print(f'Чего желаете, {name}?')
    else:
        print(f'{name}, вы лжете - в наше время столько не живут ...')