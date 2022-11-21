from random import randint


list_1 = [randint(1, 10) for _ in range(11)]


def dublicate(lst: list) -> dict:
    lst_2 = set(lst) # сортируем наш список
    dict_1 = {key: lst.count(key) for key in lst_2}
    return dict_1


print(list_1)

print(dublicate(list_1))
