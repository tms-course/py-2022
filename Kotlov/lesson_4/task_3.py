from random import randint

list_1 = [randint(1, 10) for _ in range(100000)]


def dublicate(lst: list) -> dict:
    """
    Функция считает сколько каких цифр в списке
    """
    dict_1 = {}
    for i in lst:
        dict_1[i] = dict_1.get(i, 0) + 1

    return dict_1


print(dublicate(list_1))
