"""
5. **Сделать функцию которая на вход принимает строку. Анализирует ее
исключительно методом isdigit() без доп. библиотек и переводит строку в число.
Функция умеет распознавать отрицательные число и десятичные дроби. Примеры:
-6.7     ->   Вы ввели отрицательное дробное число: -6.7
5        ->   Вы ввели положительное целое число: 5
5.4r     ->   Вы ввели не корректное число: 5.4r
-.777    ->   Вы ввели отрицательно дробное число: -0.777
"""

def check_string_for_valid_number(string: str):
    """
    Check string function
    
    :param string: string for check
    :returns: return None
    """
    string = string.strip()
    flag_negative_number, flag_fractional_number = string[0] == '-', '.' in string
    
    if string.replace('-', '', 1).replace('.', '', 1).isdigit():
        if not flag_negative_number and not flag_fractional_number:
            print(f'Вы ввели положительное целое число {string}')
        elif flag_negative_number and not flag_fractional_number:
            print(f'Вы ввели отрицательное целое число {string}')
        elif not flag_negative_number and flag_fractional_number:
            print(f'Вы ввели положительное дробное число {float(string)}')
        else:
            print(f'Вы ввели отрицательное дробное число {float(string)}')
    else:
        print(f'Вы ввели не корректное число {string}')  


check_string_for_valid_number('-.0')