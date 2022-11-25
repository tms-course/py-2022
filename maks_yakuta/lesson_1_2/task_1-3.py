from math import fabs
# task 1
a = float(input ('Введите первое число'))
b = float(input ('Введите второе число'))
print ((a+b), (a-b), (a*b), (a%b), (a**b), (a//b))

# task 2
x = 17 / 2 * 3 + 2
y = ((17 / 2) * 3) + 2
print(x, y, x==y)

x = 2 + 17 / 2 * 3
y = 2 + ((17 / 2) * 3)
print(x, y, x==y)

x = 19 % 4 + 15 / 2 * 3
y = (19 % 4) + ((15 / 2) * 3)
print(x, y, x==y)

x = (15 + 6) - 10 * 4
y = (15 + 6) - (10 * 4)
print(x, y, x==y)

x = 17 / 2 % 2 * 3 ** 3
y = ((17 / 2) % 2) * (3 ** 3)
print(x, y, x==y)

# task 3
from math import fabs
x = float(input('Введите действительное число x = '))
y = float(input('Введите действительное число y = '))
result = (fabs(x) - fabs(y)) / (1 + fabs(x+y))
print (result)



