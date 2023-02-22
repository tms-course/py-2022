from datetime import datetime
import time


def custom_func():
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


elements_1 = int(input('Введите необходимое количество элементов списка: '))
list_1 = [custom_func() for i in range(0, elements_1)]
print(list_1)
