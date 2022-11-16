from datetime import datetime
import math

"""Decorator which counts and outputs runtime of the function
"""
def calculate_time(func):
    def time(*args, **kwargs):
        time_begin = datetime.now()
        func(*args, **kwargs)
        time_end = datetime.now()
        print ("It takes", time_end-time_begin , "to calculate the function", func.__name__)
    return time 

@calculate_time
def main(a,b,c,d):
    return a+b+c+d
main(1,2,3,4)

@calculate_time
def test_annotations(name:str) -> str:
    return f'Hello, {name}'
name = str (input('Enter name: '))
test_annotations(name)

@calculate_time
def factorial(num):
     print(math.factorial(num))
factorial(23)