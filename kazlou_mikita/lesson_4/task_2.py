def factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

n = int(input('Введите число : '))   
print(factorial(n))    

    