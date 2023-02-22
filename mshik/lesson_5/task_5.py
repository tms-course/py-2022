"""
Задача 5**.

Сделать функцию которая на вход принимает строку.
Анализирует ее исключительно метод .isdigit() без доп.библиотек и переводит строку в число.
Функция умеет распознавать отрицательные числа и десятичные дроби.
"""

def get_number_from_string(str_to_check: str) -> str:
    """
    Analyzes a string and converts into a number if it's possible.
    Args:
        str_to_check (str): String which need to be validated and coverted into a number.
    Returns:
        str: String which contains a description of the number.
    Examples:
        >>> print(get_number_from_string("-6.7"))
        Вы ввели отрицательное дробное число: -6.7
        >>> print(get_number_from_string("5.4r"))
        Вы ввели не корректное число: 5.4r
    """
    is_valid_unary_minus = str_to_check[0] == "-" and str_to_check.count("-") == 1
    if is_valid_unary_minus or "-" not in str_to_check:
        filtered_chars = [char for char in str_to_check 
                          if char in {"-", "."} or char.isdigit()]
        number_sign = "отрицательное" if "-" in filtered_chars else "положительное"
        number_type = "дробное" if "." in filtered_chars else "целое"
        
        if len(filtered_chars) == len(str_to_check):
            return f"Вы ввели {number_sign} {number_type} число: {str_to_check}"
    
    return f"Вы ввели не корректное число: {str_to_check}"

print(get_number_from_string("-6.7"))
print(get_number_from_string("5"))
print(get_number_from_string("-.5-5"))
print(get_number_from_string("5.4r"))
print(get_number_from_string("-.777"))