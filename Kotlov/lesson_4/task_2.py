
num = int(input('Введите число: '))


def factorial(number: int, product=1) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)


print(f'{num}! = {factorial(num)}')

