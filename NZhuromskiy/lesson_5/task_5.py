"""
5. ** Сделать функцию которая на вход принимает строку. Анализирует её исключительно методом .isdigit()
без доп.библиотек и переводит строку в число. Функция умеет распознавать отрицательные числа и десятичные дроби.
"""

user_input = input('Введите любое число: ')


def number(string: str) -> str:
    correct_string = string[0] == "-" and string.count("-") == 1
    if correct_string or "-" not in string:
        filter_char = [char for char in string if char in {"-", "."} or char.isdigit()]
        number_character = "отрицательное" if "-" in filter_char else "положительное"
        type_of_number = "дробное" if "." in filter_char else "целое"

        if len(filter_char) == len(string):
            return f"Вы ввели {number_character} {type_of_number} число: {string}"

    return f"Вы ввели некорректное число: {string}"


print(number(user_input))
