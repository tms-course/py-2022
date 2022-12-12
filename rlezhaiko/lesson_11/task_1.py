""" 
1. Создать генератор геометрической прогрессии.
"""


def geometric_progression_generator(first_term_progression, progression_denominator, count) -> int | float:
    """ 
    Generator of geometric progression
    
    :param first_term_progression: first term of geometric progression
    :param progression_denominator: denominator of geometric progression
    :param count: number of geometric progression elements
    :returns: return int or float as a result of geometric progression
    """
    for i in range(1, count + 1):
        yield first_term_progression * progression_denominator ** (i - 1)


count = 10
generator = geometric_progression_generator(25, 2, count)
print(generator)

for _ in range(count): 
    print(next(generator))