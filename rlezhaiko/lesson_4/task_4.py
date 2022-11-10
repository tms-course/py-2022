from time import sleep
from datetime import datetime


def get_time() -> str:
    current_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    sleep(1)
    return current_time


n = int(input('Enter n: '))
my_list = [get_time() for _ in range(n)]
print(my_list)