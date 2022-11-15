from datetime import datetime


def time_decorator(function_to_decorate):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        function_to_decorate(*args, **kwargs)
        end_time = datetime.now()
        print('Время выполнения программы:', end_time-start_time, end='\n'*2)
    return wrapper


def full_name(first_name: str, last_name: str):
    """
    Full name function
    
    :param first_name: this is first name
    :param last_name: this is last name
    :returns: return None
    """
    for _ in range(100000):
        s = f'{first_name} {last_name}'
        s_reversed = s[::-1]
    

@time_decorator
def create_list(n: int):
    """
    Create list function
    
    :param n: number of elements in the list
    :returns: return None
    """
    list_tmp = [i for i in range(n)]


full_name_decorated = time_decorator(full_name)
full_name_decorated('John', last_name='Smith')

create_list(1000000)