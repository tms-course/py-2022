# не использую count,т.к это метод,а методы кроме isdigit нельзя использовать


string_number = input('Введите возможное число: ')


def number(value: str) -> bool:
    """Провека нашей строки на полное соответсвие с числом"""
    count_minus = count_odd = 0
    for i in value:  # Считаем кол-во - и .
        if i == '.':
            count_odd += 1
            if count_odd > 1:
                return False
        elif i == '-':
            count_minus += 1
            if '-' != value[0] or count_minus > 1:
                return False
        elif not i.isdigit():
            return False
    return True


def is_digit(value: str) -> str:
    """Смотрим, что число перед нами или вообще не число"""
    if number(value):
        if '.' in value:  # если число дробное
            if '-' in value:  # если число отрицательное
                return f'Вы ввели отрицательное дробное число: {float(value)}'
            else:
                return f'Вы ввели положительное дробное число: {float(value)}'
        else:  # если число целое
            if '-' in value:
                return f'Вы ввели отрицательное целое число: {int(value)}'
            else:
                return f'Вы ввели положительное целое число: {int(value)}'
    else:
        return f'Вы ввели не корректное число: {value}'


print(is_digit(string_number))
