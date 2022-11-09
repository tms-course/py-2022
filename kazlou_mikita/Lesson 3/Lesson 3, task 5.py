import random

guessed_number = random.randint(1,30)
user_name = input('Приветсвую ! Как вас зовут ?  ')

user_number = -1

while user_number != guessed_number:
    user_number = int(input(f'{user_name}, попробуйте угадать число от 1 до 30 :  '))
    if user_number > guessed_number:
        print('Загаданное число меньше, чем то, что ввели вы !')
    elif user_number < guessed_number:
        print('Загаданное число больше, чем то, что ввели вы !')
    else:
        print(f'{user_name}, поздравляю, вы угадали загадaнное число ! Это число - {guessed_number}')

        break
3