import time
from datetime import datetime
from numbers import Number
from typing import List, Dict, Hashable


# Task 1
def swap_key_value(dict_to_swap: Dict[Hashable, Hashable]) -> Dict[Hashable, Hashable]:
    return {value: key for key, value in dict_to_swap.items()}


# Task 2
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Task 3
def get_num_of_occurences(xs: List[Number]) -> Dict[Number, int]:
    occurences = {}
    for value in xs:
        if value not in occurences:
            occurences[value] = 1
        else:
            occurences[value] += 1
    return occurences


# Task 4
n_times = int(input("Сколько раз вывести время: "))
def get_timestamps_with_delay() -> List[datetime]:
    timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    time.sleep(1)
    return timestamp

timestamps = [get_timestamps_with_delay() for _ in range(n_times + 1)]