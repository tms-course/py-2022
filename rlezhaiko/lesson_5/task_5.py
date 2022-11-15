def check_string(string: str):
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
            print(f'Вы ввели положительное дробное число {str(float(string))}')
        else:
            print(f'Вы ввели отрицательное дробное число {str(float(string))}')
    else:
        print(f'Вы ввели не корректное число {string}')  


check_string('-.0')