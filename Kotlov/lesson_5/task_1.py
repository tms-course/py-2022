
number = int(input('Введите число: '))

print((lambda x: 'чётное' if x % 2 == 0 else 'нечётное')(number))
