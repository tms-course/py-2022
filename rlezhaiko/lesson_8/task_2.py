"""
2. Создать 2 класса truck и car, которые являются наследниками auto. Класс
truck имеет дополнительный обязательный атрибут max_load. Переопределенный
метод move, перед появлением надписи "move" выводит надпись "attention", его
реализацию сделать при помощи оператора super. А также дополнительный метод 
load. При его вызове происходит пауза 1 сек., затем выдается сообщение "load" и
снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут
max_speed и при вызове метода move, после появления надписи "move" должна
появиться надпись "max speed is <max_speed>". Создать по 2 объекта для каждого
из классов truck и car, проверить все их методы и атрибуты. 
"""

from time import sleep


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


class Truck(Auto):
    """
    Class Truck
    
    Creates an instance of a truck class
    """
    def __init__(self, brand: str, mark: str, age: int, max_load: int, color: str = 'Black', weight: int = 3000) -> None:
        """
        __init__ function
        
        :param self: self object of class
        :param brand: brand of truck
        :param mark: mark of truck
        :param age: age of truck
        :param max_load: max load of truck
        :param color: color of truck (default: 'Black')
        :param weight: weight of truck (default: 3000)
        :returns: return None
        """
        super().__init__(brand, mark, age, color, weight)
        self.max_load = max_load
    
    
    def move(self) -> None:
        """ 
        Move function
        
        :param self: self object of class
        :returns: return None 
        """
        print('Attention')
        super().move()
    
    
    def load(self) -> None:
        """ 
        Load function
        
        :param self: self object of class
        :returns: return None 
        """
        sleep(1)
        print('Load')
        sleep(1)


class Car(Auto):
    """
    Class Car
    
    Creates an instance of a car class
    """
    def __init__(self, brand: str, mark: str, age: int, max_speed: int, color: str = 'Black', weight: int = 2000) -> None:
        """
        __init__ function
        
        :param self: self object of class
        :param brand: brand of car
        :param mark: mark of car
        :param age: age of car
        :param max_speed: max speed of car
        :param color: color of car (default: 'Black')
        :param weight: weight of car (default: 2000)
        :returns: return None
        """
        super().__init__(brand, mark, age, color, weight)
        self.max_speed = max_speed
    
    
    def move(self) -> None:
        """ 
        Move function
        
        :param self: self object of class
        :returns: return None 
        """
        super().move()
        print(f'Max speed is {self.max_speed}')


car_1 = Car('Mercedes', 'AMG G63', 5, 300)
car_2 = Car('BMW', 'I8', 3, 320)
truck_1 = Truck('Mercedes', 'ABC', 1, 2000)
truck_2 = Truck('BMW', 'DFE', 2, 3000)
list_objects = [car_1, car_2, truck_1, truck_2]
for item in list_objects:
    print(item.__dict__)

for item in list_objects[:2]:
    item.move()
    item.stop()
    item.birthday()
    print(item.age)

for item in list_objects[2:]:
    item.move()
    item.stop()
    item.load()
    item.birthday()
    print(item.age)