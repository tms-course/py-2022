str_1 = input('Введите строку 1: ')
str_2 = input('Введите строку 2: ')
str_3 = input('Введите строку 3: ')
str_4 = input('Введите строку 4: ')


with open('best_text.txt', 'w') as f:
    f.write(f'{str_1}\n')
    f.write(f'{str_2}\n')

with open('best_text.txt', 'a') as f:
    f.write(f'{str_3}\n')
    f.write(str_4)
