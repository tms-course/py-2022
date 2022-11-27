"""  Записывает в файл json словарь, содержащий ID, имя и возраст
Имя и возраст записаны в кортеже
:param id: идентификатор в формате шестизначного числа
:param name: имя в строковом значениии
:param age: возраст в численном значении
:param dict1: данные словаря, включающие id и имя и возраст 
returns Обновленный файл json 
"""
import json
data = None


id = int(input("Enter ID: "))

for id in range (id, id+6, 1):
    if len(str(id)) == 6:
        name = str (input("Enter name: "))
        age = int(input("Enter age: "))
        dict1 = {id : (name , age)
        }     
        
        with open ('task3.json','a+') as f:
            json.dump(dict1, f,indent=2)
    
    else:
        print ("Length of ID is not equel to 6, try again")
    


