""" 
4. #classmethod #dataclass
* Пиццерии Dominus требуется написать программу, которая способна осуществлять 
заказ пицц из их фирменной коллекции(пока что там только два варианта) либо же 
покупатель может сам указать, какие из ингредиентов предложенных пиццерией добавить,
чтобы получилось все как покупатель любит. Пиццы характеризуются ингридентами
и диаметром, от этого будет зависеть и цена. Заказ может состоять из нескольких пицц.
Денег у пиццерии хватает только на консольное приложение.
"""
from  sys import stdin
from dataclasses import dataclass

menu_message = 'Введите 1 для заказа пиццы. Введите 2 для завершения заказа. Введите 3 для выхода из приложения.'
choice_message = """Введите 1 для заказа пиццы Pepperoni. Введите 2 для заказа пиццы Branded.
Введите 3 для заказа пиццы Custom(c выбором ингридиентов по вкусу). Введите 4 для выхода в главное меню"""
hello_message = f"""Вас приветствует пиццерия Dominus!
{menu_message}"""
error_message = f"""Такой команды не существует!
{menu_message}"""
print(hello_message)


@dataclass
class Ingredients():
    base: float = 13.25
    meat: float = 1.99
    chiken: float = 1.57
    tomato: float = 0.89
    mushrooms: float = 0.99
    pepper: float = 0.95
    bacon: float = 3.23
    chilli: float = 2.10
    cheese: float = 1.56


@dataclass
class Pizzas():
    pepperoni: float = 25.56
    branded: float = 30.91
    

@dataclass
class Sizes():
    small_size: float = 0.6
    middle_size: float = 0.75
    large_size: float = 1.0
    family_size: float = 1.3


class User(object):
    summ = 0.0
    cart = {}
    """
    Class User
    
    Creates an instance of a User class
    """
    def __init__(self, name: str = '', phone_number: str = '') -> None:
        """ 
        __init__ function
        
        :param self: self object of class
        :param name: name
        :param phone_number: phone number
        :returns: return None 
        """
        self.name = name
        self.phone_number = phone_number
    
    
    @classmethod
    def custom_pizza(cls, ingredients, sizes):
        print(ingredients.__dict__)
        summ = ingredients.base
        summ += ingredients.meat
        summ *= sizes.small_size
        cls.summ += summ
        print(cls.summ)
    
    
    @classmethod
    def pizza_1(cls, pizzas, sizes):
        print(pizzas.__dict__)
        summ = pizzas.pepperoni * sizes.small_size
        cls.summ += summ
        print(cls.summ)
    
    
    @classmethod
    def pizza_2(cls, pizzas, sizes):
        print(pizzas.__dict__)
        summ = pizzas.branded * sizes.small_size
        cls.summ += summ
        print(cls.summ)


def make_order():
    flag_exit = False
    print(choice_message)
    while not flag_exit:
        for line in stdin:
            line = line.strip()
            if line == '1':
                pass
            elif line == '2':
                pass
            elif line == '3':
                pass
            elif line == '4':
                flag_exit = True
                break
            else:
                print('Такой команды не существует!', choice_message, sep='\n')
            
    print(menu_message)
    


def finish_order(user):
    print(user.summ)
    print(menu_message)


for line in stdin:
    user = User()
    line = line.strip()
    if line == '1':
        make_order()
    elif line == '2':
        finish_order(user)
    elif line == '3':
        del user
        break
    else:
        print(error_message)