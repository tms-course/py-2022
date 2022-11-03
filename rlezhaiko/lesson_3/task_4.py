# Вариант № 1 (Цикл for)
n, summ = int(input('Введите целое число: ')), 0

for i in range(1, n+1):
    summ += i**3

print(f'Сумма кубов: {summ}')



# Вариант № 2 (Цикл while)
n, summ, i= int(input('Введите целое число: ')), 0, 1

while i <= n:
    summ += i**3 
    i += 1

print(f'Сумма кубов: {summ}')