# 1st task
words = input('введите 2 слова:').split()
print('!{} ! {}!'.format(words[1], words[0]))
print(f'!{words[1]} ! {words[0]}!')
print('!{0} ! {1}!'.format(words[1], words[0]))

# 2-3 task
while True:
    name = input('Введите свое имя: ')
    age = input('Введите свой возраст: ')
    if age == 'exit':
        break
    elif not age.isdigit() or int(age) <= 0:
        print('Ошибка, повторите ввод')
    elif int(age) > 0 and int(age) < 10:
        print('Привет, шкет', name)
    elif int(age) >= 10 and int(age) <=18:
        print('Как жизнь, ', name)
    elif int(age) > 18 and int(age) < 100:
        print('Что желаете, ', name, '?')

    elif int(age) > 100:
        print(name, 'вы лжете - в наше время столько не живут...')


# 4task
n = int(input('введите число: '))
result = 0
for i in range(n + 1):
    result += i**3
print(result)

n = int(input('введите число: '))
result = 0
x = 0
while x <= n:
    result += x**3
    x += 1
print(result)

# 5 task
import random
n = random.randint(0, 10)
while True:
    number = int(input('Угадайте число:'))
    if number == n:
        print('тебе улыбнулась удача')
        break
    if number > n:
        print('выбери число меньше')
    elif number < n:
        print('выбери число больше')