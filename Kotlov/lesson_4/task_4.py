from datetime import datetime, timedelta

number_date = int(input('Количество дат в списке: '))


def now_time(delay: int) -> str:
    return datetime.strftime(datetime.now()+timedelta(seconds=delay), '%Y-%m-%d %H:%M:%S')


lst = [now_time(delay) for delay in range(number_date)]

print(lst)

