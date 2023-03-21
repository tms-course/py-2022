def geometric_progression(base: int, denominator: int) -> int:
    n = 0

    while True:
        yield base * denominator ** n
        n += 1


g = geometric_progression(2, 2)
for _ in range(10):
    print(next(g))