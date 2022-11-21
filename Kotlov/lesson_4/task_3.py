from random import randint


list_1 = [randint(1, 10) for _ in range(11)]


def _set_(lst: list) -> list:
    """Функция помещает в новый список все уникальные числа из полученного списка """
    lst_2 = []
    [lst_2.append(i) for i in lst if i not in lst_2]
    return lst_2


def dublicate(lst: list) -> dict:
    """
    Функция считает сколько каких цифр в списке
    """
    lst_2 = _set_(lst)
    dict_1 = {key: lst.count(key) for key in lst_2}
    return dict_1


print(list_1)

print(dublicate(list_1))
