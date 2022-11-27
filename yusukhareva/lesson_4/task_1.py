"""Меняем местами ключи и значения словаря
:param dict_orig: функция, разбирающая входящий словарь
:param d_swap: измененный словарь
"""
def dict_orig(**kwargs):
    return {v: k for k, v in kwargs.items()}

d_swap = dict_orig(a= "Anna", b = "Boris")
print(d_swap)