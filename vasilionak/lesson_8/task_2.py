"""Создать 2 класса truck и car, которые являются наследника класса auto. Класс truck имеет дополнительный
обязательный атрибут max_loadю Переопределенный метод move, перед поялвнием надпии move выводит attention
его реализацию сделать при помощи оператра super. А так же дополнительный метод load. при его вызове
происходит пауза 1 сек., затем выдается сообщение load и снова пауза 1 сек. Класс car имеет дополнительный
обязательный фтрибут max_spead и при вызове метода move после появления надписи moveдолжна появиться
надпись max_speed is <max_speed>. Создать по 2 объекта для каждого из классов и провреить все их методы и атрибуты"""


import time


class Auto:
"""
Base class Auto
    Attributes:
    brand: str 
    age: int 
    mark: int 
    color: str = None 
    weight: float = None
    
    Methods:
        move(): Print move
        stop(): Print stop
        birthday(): Increases an age by one
        """


    def __init__(self, brand: str, age: int, mark: str, color: str = None, weight: float = None) -> None:
        """
        Initialisation of Auto object
        :param brand: Auto's brand
        :param age: Auto's age
        :param mark: Auto's mark
        :param color: Auto's color, None by default
        :param weight: Auto's weight, None by default
        """
        
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
    """Print move"""
        print("move")

    def stop(self):
    """Print stop"""
        print("stop")

    def birthday(self):
    """Increases an age by one"""
        self.age += 1
        print(self.age)


class Truck(Auto):
"""
Inherited class Truck
    Attributes:
    brand: str 
    age: int 
    mark: int
    max_load: float
    color: str = None 
    weight: float = None
    
    Methods:
        move(): Prints attention, then move
        load(): Sleeps for a second, then print load, after sleeps 1 more second
        """

    def __init__(self, brand: str, age: int, mark: str, max_load: float, color: str = None, weight: float = None) -> None:
        """
        Init Truck object
        :param brand:
        :param age:
        :param mark:
        :param max_load:
        :param color:
        :param weigth:
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
    """Prints attention, then move"""
        print('Atention')
        super().move()

    def load(self):
    """Sleeps for a second, then print load, after sleeps 1 more second"""
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
"""
Inherited class Car
    Attributes:
    brand: str 
    age: int 
    mark: int
    max_speed: int
    color: str = None 
    weight: float = None
    
    Methods:
        move(): Print max_speed
        """
       
    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = None, weight: float = None) -> None:
        """
        Init Truck object
        :param brand:
        :param age:
        :param mark:
        :param max_speed:
        :param color:
        :param weigth:
        """
        
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
    """Print max_speed"""
        super().move()
        print(f'Max speed {self.max_speed}')

Ferrari = Car('Ferrari', 17, '360', 210)
Porsche = Car('Porsche', 7, '911', 200, 'black', 1.700)
Hyundai = Truck('Hyundai', 5, '254', 362.2, 'white', 1.500)
Honda = Truck('Honda', 9, '657', 180, )

Ferrari.move()
Ferrari.stop()
Ferrari.birthday()
print(Ferrari.__dict__)

Hyundai.move()
Hyundai.load()
Hyundai.birthday()
print(Hyundai.__dict__)



