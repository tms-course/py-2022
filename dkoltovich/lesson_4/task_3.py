def count_elements(some_lst: list) -> dict:
    counter_dict = {}
    for number in some_lst:
        counter_dict[number] = counter_dict.get(number, 0) + 1

    return counter_dict


lst = [1, 2, 3, 1, 2, 1, 2, 4, 5, 5, 5, 5]
print(count_elements(lst))
