# Цикл for
number = int(input('Введите целоe число: '))
suma = 0
for i in range(1, number+1):
    suma += i**3

print(f'Ваша сумма = {suma}')

# Цикл while
number = int(input('Введите целоe число: '))
suma, i = 0, 1
while i <= number:
    suma += i**3
    i += 1

print(f'Ваша сумма = {suma}')
