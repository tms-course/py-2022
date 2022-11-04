from random import randint

hidden_number = randint(1, 100) # от 1 до 100 включительно
print('Игра угадайка. Программа загадала число от 1 до 100 включительно. Попробуйте угадать число!')

while True:
    user_number = int(input('Введите число от 1 до 100 включительно. '))
   
    if user_number < hidden_number:
        print('Загаданное число больше!')
    elif user_number > hidden_number:
        print('Загаданное число меньше!')
    else:
        print(f'Верно! Вы угадали загаданное число. Загаданное число: {hidden_number}.')
        break