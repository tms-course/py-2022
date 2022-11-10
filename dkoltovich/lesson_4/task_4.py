import time
from datetime import datetime


def time_list_generator(n: int) -> list:
    time.sleep(1)
    tmp_list = []
    for i in range(n):
        tmp_list.append(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        time.sleep(1)

    return tmp_list


n = int(input('Введите кол-во элементов списка: '))
lst = [i for i in time_list_generator(n)]
print(lst)
