from random import randint

a = int(input('Введите начальное число для диапазона: '))
b = int(input('Введите конечное число для диапазона: '))

c = randint(a, b)  # Наше случайное число

try_count = 1

while True:
    your_number = int(input('Введите возможное число: '))
    if your_number < c:
        print('Ваше число меньше загаданного!')
        try_count += 1
    elif your_number > c:
        print('Ваше число больше загаданного!')
        try_count += 1
    else:
        print(f'Ура!!! Вы угадали - это число {c}\nВы угадали за {try_count} попыток.')
        break
