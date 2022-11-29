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
def add_str(x) -> str:
    f = ''
    if len(x) != len(list(filter(lambda f:  f.isdigit() or f == '.' or f == '-', x))):
        return f'Вы ввели некорректное число: {x}'
    if x[0] == '-':
        f = 'отрицательное'
    else:
        f = 'положительное'

    if x[1::].find('-') != -1:
        return f'Вы ввели некорректное число: {x}'
    if x.find('.') != -1:
        return f'Вы ввели {f} дробное число: {x}'
    return f'Вы ввели {f} целое число:  {x}'
while True:
    x = input('введите число:')
    print(add_str(x))


















































def analyze_string_number(string_number: str) -> str:
    is_minus_on_correct_place = (
            (string_number[0] == '-' and string_number.count('-') == 1) or
            (string_number[0] != '-' and string_number.count('-') == 0)
    )

    valid_chars = list(filter(lambda x: (x.isdigit() or x == '.' or x == '-'), string_number))
    if len(valid_chars) < len(string_number) or not is_minus_on_correct_place:
        return f'Вы ввели не корректное число {string_number}'

    sign = 'положительное' if string_number[0] != '-' else 'отрицательное'
    if string_number.find('.') != -1:
        return f'Вы ввели {sign} дробное число {float(string_number)}'

    return f'Вы ввели {sign} целое число {int(string_number)}'


while True:
    n = str(input())
    print(analyze_string_number(n))