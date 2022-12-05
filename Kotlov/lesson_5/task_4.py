from datetime import datetime

number = int(input('Введите число: ')) # чтобы в будущем сделать список до этого числа


def check_time(func):
    """Декоратор отвечает за время выполнения"""
    def wrapper(*args):
        start = datetime.now()
        res = func(*args)
        print(datetime.now() - start)
        return res
    return wrapper


@check_time
def list_for(num: int) -> list:
    lst = []
    for i in range(num):
        lst.append(i)
    return lst


@check_time
def list_generator(num: int) -> list:
    lst = [i for i in range(num)]
    return lst


l1 = list_for(number)
l2 = list_generator(number)
