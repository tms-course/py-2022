"""
Декоратор к функциям, который считает и выводит время их выполнения.
"""
from datetime import datetime


def duration_time_test(func):

    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        end_time = datetime.now()
        print(func(*args, **kwargs))
        print('время выполнения функции: ', end_time - start_time, 'сек')
        return func

    return wrapper


def factorial(n: int) -> int:
    """
    Calculates the factorial
    :param n: number whose factorial we need to know
    :return: factorial n
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


my_dict = {1: 'one', 7: 'seven', 5: 'five'}


def key_value_swap(dictionary: dict) -> dict:
    """
    Swaps keys and values
    :param dictionary: some dictionary
    :return: dictionary with keys and values swapped
    """
    return {v: k for k, v in dictionary.items()}


new_dict = key_value_swap(my_dict)


factorial = duration_time_test(factorial)(5)
key_value_swap = duration_time_test(key_value_swap)(my_dict)
