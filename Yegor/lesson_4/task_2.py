def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


n = int(input('введите число:'))
print(factorial(n))
