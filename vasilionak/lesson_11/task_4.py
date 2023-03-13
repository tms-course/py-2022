"""Сделать функцию валидации email адрусов при помощи регулярных выражений.
Общий вид email адреса 'username@hostname':
(a)username можеть состоять из латиницы, цифр, таких как !#%&'*+-/=?^_`{~}|
и точки, за исключением первого и последнего знака, которая не может
повторяться.
(b) hostname состоит из нескольких компонентов, разделенных точкой и не 
превышающих 63 символа. Компоненты, в свою очередь, состоят из латинских 
букв, цифр и дефисов, причем дефисы не могут быть в начале или в конце 
компонента."""

import re

regex = re.compile(r"([^.](\.?[\d\w!#%&'*+-=/?^_{}|~])+)@([^\-]([\w\d\-]{1,63}\.?)+[^\-\.]$)")

def is_valid(email):
    """Check email for valid"""
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

is_valid("name.surname@gmail.com")
is_valid("name.surname@gmail.com-")
is_valid("33anonymous123@yahoo.co.uk")
is_valid("anonymous123@-yahoo.co.uk")
