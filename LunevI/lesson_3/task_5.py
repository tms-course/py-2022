import random

max_border = 10
min_border = 1
print(f'Загадайте число от {min_border} до {max_border}')

while True:
    if max_border == min_border:
        print(f'Ваше число {max_border}')
        break

    number = random.randint(min_border, max_border)
    print(f'Ваше число больше {number}?')
    answer = input('да/нет')
    if answer == 'да':
        min_border = number + 1
    else:
        max_border = number
