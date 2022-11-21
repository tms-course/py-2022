name = input('Введите имя: ')
age = int(input("Возраст: "))

if age <= 0 or str(age).isalpha():
    print('Ошибка, повторите ввод')
elif 0 < age < 10:
    print(f'Привет, шкет {name}')
elif 10 <= age <= 18:
    print(f'Как жизнь {name}?')
elif 18 < age < 100:
    print(f'Что желаете {name}?')
else:
    print(f'{name}, вы лжёте - в наше время столько не живут...')
