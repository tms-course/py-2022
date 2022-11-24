"""
1. Создать родительский класс auto, у котторого есть атрибуты: brand, age, color, mark
и weight. А также методы: move, birthday и stop. Методы move и stop выводят
сообщение на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
Атрибуты brand, age, mark являются обязательными при объявлении объекта. 
"""

class Auto(object):
    """
    Class Auto
    
    Creates an instance of a auto class
    """
    def __init__(self, brand: str, mark: str, age: int, color: str = 'Black', weight: int = 2000) -> None:
        """ 
        __init__ function
        
        :param self: self object of class
        :param brand: brand of auto
        :param mark: mark of auto
        :param age: age of auto
        :param color: color of auto (default: 'Black')
        :param weight: weight of auto (default: 2000)
        :returns: return None 
        """
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight
    
    
    def move(self) -> None:
        """ 
        Move function
        
        :param self: self object of class
        :returns: return None 
        """
        print('Move')
    
    
    def stop(self) -> None:
        """ 
        Stop function
        
        :param self: self object of class
        :returns: return None 
        """
        print('Stop')
    
    
    def birthday(self) -> None:
        """ 
        Birthday function
        
        :param self: self object of class
        :returns: return None 
        """
        self.age += 1


a = Auto('Mercedes', 'AMG G63', 5)
a.move()
a.stop()
a.birthday()
print(a.age)
        