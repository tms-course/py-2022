import time
from datetime import datetime

number_date = int(input('Количество дат в списке: '))


def now_time() -> str:
    timer = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    time.sleep(1)
    return timer


lst = [now_time() for _ in range(number_date)]

print(lst)
