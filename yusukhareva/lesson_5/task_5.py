"""
Перевод строки в число и проверка, дробное оно или целое (отрицательные целые числа будут относиться к дробным отрицательным)
:param num_to_check: число, которое нужно проверить 
:param dot_count: количество точек в строке
:param dot_pos: позиция точки в строке
:param pos_0_dot: элементы с нулевой позиции до позиции точки
:param pos_1_dot: элементы с первой позиции до позиции точки
:param pos_dot_end: элементы с позиции точки и до конца строки 
returns Число целое, либо дробное положительно, либо дробное отрицательное, либо ошибка
"""

def str_check(num_to_check: str):
    dot_count = num_to_check.count('.')
    dot_pos = num_to_check.find('.')
    pos_0_dot = num_to_check[1:dot_pos-1]
    pos_1_dot = num_to_check[0:dot_pos-1]
    pos_dot_end = num_to_check[dot_pos+1:len(num_to_check)]

    if num_to_check.isdigit():
        print ( "Вы ввели положительное целое число: ", num_to_check)
    elif num_to_check[0] == "-" and dot_count == 1 and (pos_1_dot.isdigit() or pos_1_dot == ""):
        if pos_dot_end.isdigit():
            print ("Вы ввели отрицательное дробное число: ", num_to_check)    
        
        elif pos_dot_end== "" and num_to_check != "-.":        
            print ( "Вы ввели отрицательное целое число: ", num_to_check)      

    elif dot_count == 1 and (pos_0_dot.isdigit() or pos_0_dot == ""):
        if pos_dot_end.isdigit():
            print ("Вы ввели положительное дробное число: ", num_to_check)
        elif pos_dot_end == "" and num_to_check != ".":
            print ( "Вы ввели положительное целое число: ", num_to_check)
        
    else:
        print ("Вы ввели некорректное число: ", num_to_check)
            
str_check(input())