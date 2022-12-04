"""
Перевод строки в число и проверка, дробное оно или целое (отрицательные целые числа будут относиться к дробным отрицательным)
:param num_to_check: число, которое нужно проверить 
returns Число целое, либо дробное положительно, либо дробное отрицательное, либо ошибка
"""
def str_check(num_to_check: str):
    if num_to_check.isdigit():
        print ( "Вы ввели целое число: ", num_to_check)
    else:   
        try:
            num_to_check = float(num_to_check) 
            if num_to_check < 0:
                print ("Вы ввели отрицательное дробное число: ", num_to_check)
            elif num_to_check > 0:
                print ("Вы ввели положительное дробное число: ", num_to_check)
        except:
            print ("Вы ввели некорректное число: ", num_to_check)
    
str_check(input())