def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)

