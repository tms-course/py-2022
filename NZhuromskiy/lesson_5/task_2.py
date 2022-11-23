"""
2. Дан список чисел. Вернуть список, где при помощи функции map() каждое число переведено в строку. В качестве функции
в map использовать lambda.
"""

numbers = [1, 2, 3, 4, 5]

count = list(map(lambda num: str(num), numbers))

print(count)
