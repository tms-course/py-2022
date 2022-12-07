"""
Задание 1.

Создать генератор геометрической прогрессии.
"""

def geometric_progression(first_term: int, denominator: int, ordinal_num: int) -> int:
    """
    Generates geometric progression.
    Formula: b * q ^ (n - 1)

    Args:
        first_term (int): 1th Term of the Arithmetic Sequence
        denominator (int): Denominator
        ordinal_num (int): Ordinal number, which indicates the position

    Yields:
        Geometric progression (int)
    """
    for n in range(1, ordinal_num + 1):
        yield first_term * denominator ** (n - 1)


print([x for x in geometric_progression(21231, 5, 10)])

