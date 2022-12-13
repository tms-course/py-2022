""" Check even or odd number is entered

:param num: the number needed to check
:param num_to_check: calling the number to check even it's odd or even
:returns: even or odd
"""

num = int(input("Enter number to check: "))
print((lambda num: 'even' if num % 2 == 0 else 'odd')(num))