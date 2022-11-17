def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


print(factorial(n=int(input('введите число:'))))



