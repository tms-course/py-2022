def recursion(n: int) -> int:
    if n == 1:
        return 1
    return n * recursion(n-1)


n = int(input('Enter n: '))
print(recursion(n))