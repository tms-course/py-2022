def recurs (n):
    if n == 0: 
        return 1
    return n * recurs(n-1)

print (recurs (10))