"""
Задание 4.

Написать декоратор к 2-м любым функциям, которые бы считали и выводили время
их выполнения.
"""
import time
from datetime import datetime
from functools import wraps
from typing import Callable, List, Iterable


def timer(func: Callable) -> Callable:
    """Decorator to measure an execution time"""
    @wraps(func)
    def inner(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return inner


@timer
def flatten(items: List) -> List:
    """
    Converts a multi-dimensional List into a 1-dimensional List
    Args:
        items (List): Multi-demensional list   
    Returns:
        result (List): A flattened version of the original list
    Examples:
        >>> print(flatten([1, 2, 3, [4, 5, 6, [8, 9, 10, [3], 12, 13]]]))
        [1, 2, 3, 4, 5, 6, 8, 9, 10, 3, 12, 13]
    """
    result = []
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, (bytes, str)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, 2, 3, [4, 5, 6, [8, 9, 10, [11, 17, 19], 12, 13], 19, 21, [12,13]], 133]))


@timer
def sleep_n_seconds(n: float) -> None:
    """
    Function sleeps n seconds
    
    Args:
        n (int): Delay execution for a given number of seconds 
    """
    print(f"Sleeping for {n} seconds..")
    time.sleep(n)

print(sleep_n_seconds(1.3))
