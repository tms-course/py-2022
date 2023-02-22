""" 
1. Создать генератор геометрической прогрессии.
"""


def geometric_progression_generator(first_term: int | float, denominator: int | float, count: int) -> int | float:
    """
    :param first_term_: first term of geometric progression
    :param denominator: denominator of geometric progression
    :param count: number of geometric progression elements
    :returns: return int or float as a result of geometric progression
    """
    for i in range(1, count + 1):
        yield first_term * denominator ** (i - 1)


count = 10
generator = geometric_progression_generator(25, 2, count)
print(generator)

for num in generator:
    print(num)