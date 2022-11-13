def get_factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * get_factorial(n-1)


n = int(input('Enter n: '))
print(get_factorial(n))