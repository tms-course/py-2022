"""
Задание 1.
Создать генератор геометрической прогрессии.
"""


def geometrical_progression(first: int, denominator: int, n: int):
    """
    Geometrical progression generator
    :param first: first term of progression
    :param denominator: progression's denominator
    :param n: last term of progression
    :yield: i-th term of geometrical progression
    """

    for i in range(1, n + 1):
        b_i = first * denominator ** (i - 1)
        yield b_i
    # i = 1
    # while i != n + 1:
    #    b_i = first * denominator ** (i - 1)
    #   yield b_i
    #   i += 1


progression = geometrical_progression(2, 4, 5)
while True:
    print(next(progression))
