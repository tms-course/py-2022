list_1 = [1, 2, 3, 4, 1, 1, 3, 2]


def custom_dict(lst: list) -> dict:
    dict_new = {}
    for elements in lst:
        dict_new[elements] = dict_new.get(elements, 0) + 1
    return dict_new


print(custom_dict(list_1))
