""" Check even or odd number is entered

:param x: the number to check
:returns: even or odd
"""

print("even") if (lambda x: x%2)(int(input("Enter number to check: " ))) == 0 else print("odd")