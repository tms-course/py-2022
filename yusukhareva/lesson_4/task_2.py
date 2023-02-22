"""
Выводит факториал числа
:param num_factorial: функция, вычисляющая факториал числа
"""

def num_factorial (n):
    if n == 0: 
        return 1
    return n * num_factorial(n-1)

print (num_factorial (10))