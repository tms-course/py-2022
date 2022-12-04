"""
Task_4, Lesson_5
Написать декоратор к 2-м любым функциям, которые бы считали и выводили время их выполнения.
"""
from datetime import datetime
def print_str(string):
    print(string)
    print('hello world')

def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)

def decorator(func):
    def wrapper(*args):
        time = datetime.now()
        func(*args)
        end_time = datetime.now()
        return end_time-time
    return wrapper
print(decorator(print_str)(5))
print(decorator(fact)(5))

