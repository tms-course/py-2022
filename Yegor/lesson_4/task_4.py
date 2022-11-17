from datetime import datetime
import time


def func():
    time.sleep(1)
    return datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')


n = int(input('введите кол-во элементов:'))
random_list = [func() for j in range(0, n)]
print(random_list)
