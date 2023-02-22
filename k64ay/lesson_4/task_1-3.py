from typing import List

# Task 1 - swap key value
example_dict = {'a': 1, 'b': 2, 'c': 3}

print({value: key for key, value in example_dict.items()})

# Task 2 - factorial
def fact(n: int) -> int:
    if n == 1:
        return 1
    return n * fact(n - 1)

# Task 3 - count same numbers
def count_same_nums(nums: List[int]) -> dict:
    count_map = {}
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1

    return count_map

