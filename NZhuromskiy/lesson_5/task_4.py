"""
4. Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
"""

from datetime import datetime


def decorating_func(own_func):
    def wrapper(*args):
        start = datetime.now()
        print(own_func(*args))
        print(datetime.now() - start)

    return wrapper


@decorating_func
def custom_func(num_1, num_2):
    return num_1 + num_2


@decorating_func
def custom_func_2(num_1, num_2):
    return num_1 * num_2


print(custom_func(2, 5), custom_func_2(3, 5))
