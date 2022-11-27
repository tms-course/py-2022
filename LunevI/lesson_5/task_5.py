"""
Сделать функцию которая на вход принимает строку. Анализирует ее
исключительно методом isdigit() без доп. библиотек и переводит строку в число.
Функция умеет распознавать отрицательные число и десятичные дроби. Примеры:
-6.7     ->   Вы ввели отрицательное дробное число: -6.7
5        ->   Вы ввели положительное целое число: 5
5.4r     ->   Вы ввели не корректное число: 5.4r
-.777    ->   Вы ввели отрицательно дробное число: -0.777
"""

enter_number = input('Введите ваше число: ')


def check_string(string: str):
    string = string.strip()
    negative_number, float_number = string[0] == '-', '.' in string

    if string.replace('-', '', 1).replace('.', '', 1).isdigit():
        if not negative_number and not float_number:
            print(f'Вы ввели положительное целое число {string}')

        elif not negative_number and float_number:
            print(f'Вы ввели дробное число {string}')

        elif negative_number and not float_number:
            print(f'Вы ввели отрицательное число {float(string)}')

        else:
            print(f'Вы ввели отрицательное дробное число {float(string)}')

    else:
        print(f'Вы ввели некорректное число {string}')


check_string(enter_number)
