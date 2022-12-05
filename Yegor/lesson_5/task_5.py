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
    if numbers[0] == '-':
        sign_of_number = 'отрицательное'
    else:
        sign_of_number = 'положительное'
    if len(numbers) != len(list(filter(lambda f: f.isdigit() or f == '.' or f == '-', numbers))) or (numbers[1::].find('-') != -1):
        return f'Вы ввели некорректное число: {numbers}'
    for char in numbers[1:]:
        if char == '.':
            return f"Вы ввели {sign_of_number} дробное число: {numbers}"
    return f"Вы ввели {sign_of_number} целое число: {numbers}"


while True:
    numbers = input('введите число:')
    print(analyze_number(numbers))