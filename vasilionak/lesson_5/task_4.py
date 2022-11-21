"""
написать декоратор который считает и выводит время выполения функций
"""

from datetime import datetime

def timer(decorate_function):
    def wrapped(*args, **kwargs):
        start_time = datetime.now()
        result = decorate_function(*args, **kwargs)
        print(datetime.now() - start_time)
        return result
    return wrapped

@timer
def flipped_dictionary(**kwargs):
    return {v: k for k, v in kwargs.items()}

new_dict = flipped_dictionary(a=5, b=7, c=9)

print(new_dict)

@timer
def count_element(my_list: list):
    count_map = {}
    for element in my_list:
        count_map[element] = count_map.get(element, 0) + 1

    return count_map

list = [1, 8, 1, 4, 8, 1, 6, 6, 8, 1, 5, 9]
print(count_element(list))
