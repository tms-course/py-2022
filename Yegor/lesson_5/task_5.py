"""
Task_5, Lesson_5
**Сделать функцию которая на вход принимает строку. Анализирует ее
исключительно методом isdigit() без доп. библиотек и переводит строку в число.
Функция умеет распознавать отрицательные число и десятичные дроби. Примеры:
-6.7     ->   Вы ввели отрицательное дробное число: -6.7
5        ->   Вы ввели положительное целое число: 5
5.4r     ->   Вы ввели не корректное число: 5.4r
-.777    ->   Вы ввели отрицательно дробное число: -0.777
"""
def analyze_number(numbers: str) -> str:
    numbers_sign = 0
    numbers_sign2 = 0
    if len(numbers) != len(list(filter(lambda f: f.isdigit() or f == '.' or f == '-', numbers))) or (
            numbers[1::].find('-') != -1):
        return f'Вы ввели некорректное число: {numbers}'
    for char in numbers:
        if char == '.':
            numbers_sign = 1
        if char == '-':
            numbers_sign2 = 1
    if numbers_sign == 1 and numbers_sign2 == 1:
        return("Вы ввели отрицательное дробное число")
    if numbers_sign == 1 and numbers_sign2 != 1:
        return ("Вы ввели положительное дробное число")
    if numbers_sign2 == 1:
        return("Вы ввели отрицательное целое число")
    else:
        return ("Вы ввели положительное целое число")
while True:
    numbers = input('введите число:')
    print(analyze_number(numbers))