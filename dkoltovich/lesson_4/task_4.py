import time
from datetime import datetime


def time_list_generator(n: int) -> list:
    tmp_list = []
    for i in range(n):
        tmp_list.append(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        time.sleep(1)

    return tmp_list


number_of_elements = int(input('Введите кол-во элементов списка: '))
time_list = [i for i in time_list_generator(number_of_elements)]
print(time_list)
