import time
from datetime import datetime

n = int(input('Необходимое количество элементов: '))


def current_time() -> str:
    current_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    time.sleep(1)
    return current_time


list = [current_time() for i in range(n)]
print(list)