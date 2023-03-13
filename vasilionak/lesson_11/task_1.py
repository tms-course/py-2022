"""
создать генератор геометрической прогрессии
"""
def geometric_progression(a: int, q: int, n: int):
    """
    a: first
    q: progression_denominator
    n: calculated value
    """
    for n in range(1, n + 1):
        yield a * q ** (n - 1)


g = geometric_progression(3, 6, 12)
for i in g:
    print(i)




    
    



