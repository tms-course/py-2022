import datetime
import random


def factorial(n: int) -> int:
    """
    Counts n factorial
    :param n: number whose factorial we want to count
    :return: factorial of number n
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def random_list_sum(n: int) -> int:
    """
    Generate list of random int elements in range(0,100) and counts its sum
    :param n: size of the list
    :return: sum of list's elements
    """
    rand_list = [random.randint(0, 100) for i in range(n)]
    return sum(rand_list)


def print_executing_time(func):
    """
    Decorator that counts and prints time of executing of any function
    :param func: function whose executing time we want to count
    :return:
    """
    def wrapper(*args):
        start_time = datetime.datetime.now()
        print(func(*args))
        print(datetime.datetime.now() - start_time)

    return wrapper


print_executing_time(factorial)(800)
print_executing_time(random_list_sum)(1000)
