"""  Записывает в файл json словарь, содержащий ID, имя и возраст
Имя и возраст записаны в кортеже
:param id: идентификатор в формате шестизначного числа
:param name: имя в строковом значениии
:param age: возраст в численном значении
:param input_dict: вводимый словарь, включающий в себя 6 записей по id и имя и возраст 
returns Обновленный файл json 
"""
import json
data = None
input_dict = {}
id = int(input("Enter ID: "))
if len(str(id)) == 6:
    for _ in range (6):
        name = str (input("Enter name: "))
        age = int(input("Enter age: "))
        input_dict.update({id : (name , age)})
        id +=1
else:
    print ("Length of ID is not equel to 6, try again")

with open ('task3.json','w') as f:
    json.dump(input_dict, f , indent=2)



