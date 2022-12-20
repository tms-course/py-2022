import datetime as dt
import time

def delayed_datetime():
    time.sleep(1)

    return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

elements_count = int(input('Enter elements count:'))
print([delayed_datetime() for _ in range(elements_count)])
