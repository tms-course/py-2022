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
    if len(numbers) == 0:
        return f'Вы ввели пустую строку, повторите ввод.'
    first_char = numbers[0]
    if first_char == '-':
        numbers_sign = 'отрицательное'
    else:
        numbers_sign = 'положительное'
    if (first_char != '.' and not first_char.isdigit() and first_char != '-') or (first_char == '.' and len(numbers) == 1):
        return f'Вы ввели неккоректное число: {numbers}'
    temp_answer = ''
    for char in numbers[1:]:
        if char == '.':
            temp_answer = f'Вы ввели {numbers_sign} дробное число: {numbers}'
        if not char.isdigit()  and char != '.':
            return f'Вы ввели неккоректное число: {numbers}'
    if first_char == '.':
        temp_answer = f'Вы ввели {numbers_sign} дробное число: {numbers}'
    if temp_answer != '':
        return temp_answer
    return f'Вы ввели {numbers_sign} целое число: {numbers}'
while True:
    numbers = input('введите число:')
    print(analyze_number(numbers))