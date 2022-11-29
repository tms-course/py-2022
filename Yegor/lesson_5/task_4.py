"""
Task_4, Lesson_5
Написать декоратор к 2-м любым функциям, которые бы считали и выводили время их выполнения.
"""
from datetime import datetime
def func_1(x):
    print(x)
    print('hello world')

def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)

def decorate(x):
    def func_2(*args):
        time = datetime.now()
        x(*args)
        end_time = datetime.now()
        return end_time-time
    return func_2
print(decorate(func_1)(5))
print(decorate(fact)(5))

