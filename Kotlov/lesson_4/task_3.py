from random import randint

list_1 = [randint(1, 10) for _ in range(11)]


def dublicate(lst: list) -> dict:
    """
    Функция считает сколько каких цифр в списке
    """
    dict_1 = {key: lst.count(key) for key in lst}
    return dict_1


print(list_1)

print(dublicate(list_1))
