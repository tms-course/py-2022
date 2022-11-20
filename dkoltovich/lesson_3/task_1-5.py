
import random
# 1st task
sentence = input().split()
print('!%s ! %s!' % (sentence[1], sentence[0]))
print(f'!{sentence[1]} ! {sentence[0]}!')
print('!{1} ! {0}!'.format(sentence[1], sentence[0]))

# 2-3 task
while True:
    name = input('Введите свое имя: ')
    age = input('Введите свой возраст: ')
    if age == 'quit':
        break
    elif not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод")
    elif 0 < int(age) < 10:
        print(f"Привет, шкет {name}")
    elif 10 <= int(age) <= 18:
        print('Как жизнь, {}?'.format(name))
    elif 18 < int(age) < 100:
        print(f'Что желаете, {name}?')

    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')


# 4task

n = int(input('введите число: '))
result = 0
for i in range(n + 1):
    result += i**3

print(result)
result = 0
i = 0
while i <= n:
    result += i**3
    i += 1

print(result)

# 5 task
n = random.randint(-10, 10)
while True:
    user_input = int(input('Угадайте число: '))
    if user_input == n:
        print('Угадали!')
        break
    elif user_input > n:
        print('Нет, загаданное число меньше, попробуйте еще раз')
    else:
        print('Нет, загаданное число больше, попробуйте еще раз')
