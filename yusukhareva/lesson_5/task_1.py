""" Check even or odd number is entered

:param num_to_check: the number needed to check
:param rem_of devision: teh remainder of the devision 
:returns: even or odd
"""

num_to_check = int(input("Enter number to check: "))
print (lambda rem_of_devision: rem_of_devision%2==0)(num_to_check)

