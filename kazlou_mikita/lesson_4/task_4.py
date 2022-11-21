import time
from datetime import datetime

n = int(input('Введите количество элементов списка : '))

def get_time() -> str:
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

time_list = [get_time() for i in range(n)]
print(time_list)    
