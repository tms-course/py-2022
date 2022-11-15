"""
Implementation of function that converts string into int or double number
"""


def analyze_string_number(string_number: str) -> str:
    """
    Converts string into int or double number
    :param string_number: string we want to analyze and convert into a number
    :return: string that contains massage with converted number
    """
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
