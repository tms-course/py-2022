"""Создат родител ски класс auto, у которого есть атрибуты: brand, age, cоlor, mark,
и weight. А так же методы:move, birthday, stop. Методы move и sop выводят сообщение
 на экран "move" "stop", birthday увеличивает атрибут age на 1. Атрибуты brand, age,
 mark являются обязательными при объявлении объекта"""

class Auto:

"""Base class Auto
    Attributes:
    brand: str 
    age: int 
    mark: int 
    color: str = None 
    weight: float = None
    
    Methods:
        move(): Print move
        stop(): Print stop
        birthday(): Increases an age by one"""
    
    def __init__(self, brand: str, age: int, mark: int, color: str = None, weight: float = None) -> None:
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

Audi = Auto('Audi', 5, 5)
Audi.birthday()
print(Audi.__dict__)


