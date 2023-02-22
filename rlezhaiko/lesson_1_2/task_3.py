from math import fabs

x = float(input('Введите действительное число x: '))
y = float(input('Введите действительное число y: '))

result = (fabs(x) -fabs(y)) / (1 + fabs(x * y))
print(result)