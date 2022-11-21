
num = int(input('Введите число: '))


def factorial(number: int, product=1, i=1) -> int:
    product *= i
    i += 1
    return product if i > number else factorial(number, product, i)


print(f'{num}! = {factorial(num)}')

