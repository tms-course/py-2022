# task 1
my_dict = {1: 'one', 7: 'seven', 5: 'five'}


def key_value_swap(dictionary: dict) -> dict:
    return {v: k for k, v in dictionary.items()}


new_dict = key_value_swap(my_dict)

print(new_dict)

# task 2
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(4))

# task 3
my_list = [3, 3, 3, 4, 1, 1, 2, 1, 2, 5, 5, 2]
my_dict = {}


def element_counter(lst: list) -> dict:
    for element in lst:
        my_dict[element] = my_dict.get(element, 0) + 1

    return my_dict


print(element_counter(my_list))

# task 4
import time
from datetime import datetime

n = int(input('Введите количество элементов списка: '))


def get_current_time() -> str:
    current_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    time.sleep(1)
    return current_time


my_list = [get_current_time() for i in range(n)]
print(my_list)
