""" Принимает строку и далее распознает её, является ли введенная строка числом, если да, то каким
:param str_to_check: вводимая строка 
"""


def check (str_to_check: str):
    
    if str_to_check[0]=='-' :
        if  str_to_check.count('.') == 0 and str_to_check[1:len(str_to_check)].isdigit():
            print("Вы ввели отрицательное целое число: ", str_to_check)
        elif  str_to_check.count('.') == 1 and (str_to_check[1:str_to_check.find(".")].isdigit() or str_to_check[1:str_to_check.find(".")] == '') and str_to_check[str_to_check.find(".")+1:len(str_to_check)].isdigit():
            print("Вы ввели отрицательное дробное число: ", str_to_check)
        else: 
            print ('Вы ввели некорректное число: ', str_to_check)
             
    elif str_to_check.count('.') == 1 and str_to_check!='.' and (str_to_check[0:str_to_check.find(".")].isdigit() or str_to_check[0:str_to_check.find(".")] == '') and str_to_check[str_to_check.find(".")+1:len(str_to_check)].isdigit():
            print("Вы ввели положительное дробное число: ", str_to_check)
    elif str_to_check.count('.') == 0 and str_to_check.isdigit():
        print("Вы ввели положительное целое число: ", str_to_check)
    else:
        print ('Вы ввели некорректное число: ', str_to_check)


check(input('Введите число: '))