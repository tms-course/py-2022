"""
Задание 2.

Дан список чисел. Вернуть список, где при помощи функции map() каждое число переведено в строку.
В качестве функции в map использовать lambda.
"""
LIST_OF_NUMS = list(range(1, 15))
num_to_str = list(map(lambda num: str(num), LIST_OF_NUMS))
print(f"Numbers represented as strings: {num_to_str}")
