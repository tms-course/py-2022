"""
Task_2, Lesson_5
Дан список чисел. Вернуть список, где при помощи функции map() каждое число переведено в строку.
В качестве функции в map использовать lambda.
"""
result = map(lambda x: str(x), [1, 2, 3, 4, 5, 6])
print(list(result))