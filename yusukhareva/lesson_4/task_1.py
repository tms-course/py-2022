"""Меняем местами ключи и значения словаря
:param dict_val_and_keys: функция, разбирающая входящий словарь
:param d_swap: измененный словарь
"""
def dict_val_and_keys(**kwargs):
    return {v: k for k, v in kwargs.items()}

d_swap = dict_val_and_keys(a= "Anna", b = "Boris")
print(d_swap)
