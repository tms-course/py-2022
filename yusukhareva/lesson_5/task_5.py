#ДОДЕЛАТЬ!
"""
Перевод строки в число
:param:
:param:
returns number or error
"""
inp_str = str(input())
def numb(inp_str):
    numb = inp_str.isdigit()
    if numb == True:
        if type (inp_str) == int:
            print ( "Вы ввели целое число: ", inp_str)
        elif type(inp_str) == float and inp_str < 0:
            print ("Вы ввели отрицательное дробное число: ", inp_str)
        elif type(inp_str) == float and inp_str > 0:
            print ("Вы ввели положительное дробное число: ",inp_str)
    else:
        print ("Вы ввели некорректное число: ", inp_str)
print(numb(inp_str))