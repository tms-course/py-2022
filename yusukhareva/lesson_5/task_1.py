""" Check even or odd number is entered

:param num: the number needed to check
:param num_to_check: calling the number to check even it's odd or even
:returns: even or odd
"""

num = int(input("Enter number to check: "))
print ('odd') if (lambda num_to_check : num_to_check%2==0)(num) == False else print ('even')