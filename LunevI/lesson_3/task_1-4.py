# task 1

text = input('Введите строку из двух слов: ')
words = text.split(' ')
print('!{0} ! {1}!'.format(words[1], words[0]))

# task 2,3

while True:
    name = input('Введите свое имя: ')
    age = int(input('Введите ваш возраст: '))

    if age <= 0:
        print('Ошибка, повторите ввод')

    elif 0 < age < 10:
        print(f'Привет, шкет {name}')

    elif 10 <= age <= 18:
        print(f'Как жизнь, {name}?')

    elif 18 < age < 100:
        print(f'Что желаете, {name}?')

    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')

# task 4

n = int(input('Введите целое число: '))
a = 0
for i in range(1, n+1):
    a = a + i**3
print(a)

n = int(input('Введите целое число: '))
i = 1
a = 0
while i <= n:
    a = a + i**3
    i = i + 1
print(a)
