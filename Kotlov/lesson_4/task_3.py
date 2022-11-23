from random import randint

list_1 = [randint(1, 10) for _ in range(100000)]


def dublicate(lst: list) -> dict:
    """
    Функция считает сколько каких цифр в списке
    """
    dict_count_num = {}
    for i in lst:
        dict_count_num[i] = dict_count_num.get(i, 0) + 1

    return dict_count_num


print(dublicate(list_1))
