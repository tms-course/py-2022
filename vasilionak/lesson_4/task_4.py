import time
from datetime import datetime

number_of_elements = int(input("Сколько элементов должно быть в этом списке: "))

def date_list() -> str:
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

list = [date_list() for i in range(number_of_elements)]


print(list)

