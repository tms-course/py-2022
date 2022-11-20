"""
4. Написать декоратор к 2-м любым функциям, который бы считал и выводил время
их выполнения.
"""

from datetime import datetime
from typing import Callable


def lead_time_decorator(function_to_decorate: Callable) -> Callable:
    """
    Lead time decorator function
    
    :param function_to_decorate: this is function to decorate
    :returns: return function
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        function_to_decorate(*args, **kwargs)
        end_time = datetime.now()
        print('Время выполнения программы:', end_time-start_time, end='\n'*2)
    return wrapper


def concatenate_first_and_last_name(first_name: str, last_name: str):
    """
    Concatenate first and last name function
    
    :param first_name: this is first name
    :param last_name: this is last name
    :returns: return None
    """
    for _ in range(100000):
        s = f'{first_name} {last_name}'
        s_reversed = s[::-1]
    

@lead_time_decorator
def create_list(n: int):
    """
    Create list function
    
    :param n: number of elements in the list
    :returns: return None
    """
    list_tmp = [i for i in range(n)]


full_name_decorated = lead_time_decorator(concatenate_first_and_last_name)
full_name_decorated('John', last_name='Smith')

create_list(1000000)