"""
Перевод строки в число и проверка, дробное оно или целое (отрицательные целые числа будут относиться к дробным отрицательным)
:param num_to_check: число, которое нужно проверить 
returns Число целое, либо дробное положительно, либо дробное отрицательное, либо ошибка
"""

def str_check(num_to_check: str):
    if num_to_check.isdigit():
        print ( "Вы ввели положительное целое число: ", num_to_check)
    elif num_to_check[0] == "-" and num_to_check.count('-') == 1 and num_to_check[num_to_check.find('-')+1:len(num_to_check)].isdigit():
        print ( "Вы ввели отрицательное целое число: ", num_to_check)
    elif num_to_check[0] == "-" and num_to_check.count('-') == 1 and num_to_check.count('.') in (0,1) and num_to_check[num_to_check.find('-')+1:num_to_check.find('.')].isdigit() and num_to_check[num_to_check.find('.')+1:len(num_to_check)].isdigit():
        print ("Вы ввели отрицательное дробное число: ", num_to_check)
    elif  num_to_check.count('.') in (0,1) and num_to_check[0:num_to_check.find('.')].isdigit() and num_to_check[num_to_check.find('.')+1:len(num_to_check)].isdigit():
        print ("Вы ввели положительное дробное число: ", num_to_check)
    else:
        print ("Вы ввели некорректное число: ", num_to_check)
    
str_check(input())