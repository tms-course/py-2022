import time
from datetime import datetime


def time_list_generator() -> str:
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


number_of_elements = int(input('Введите число элементов списка: '))
time_list = [time_list_generator() for i in range(number_of_elements)]
print(time_list)
