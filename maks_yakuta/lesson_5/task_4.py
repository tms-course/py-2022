from datetime import datetime

def factorial(n: int) -> int:

    if n == 0:
        return 1
    return n * factorial(n - 1)

dct = {'a':1, 'b':3, 'c':2}

def invert (dct):
    return {val: key for key, val in dct.items()}

def lead_time(func):

    def wrapper(*args, **kwargs):
        start = datetime.now()
        end = datetime.now()
        print(func(*args, **kwargs))
        print("Время выполнения кода: ", start - end, 'сек.')

    return wrapper

lead_time(factorial)(5)
lead_time(invert)(dct)






