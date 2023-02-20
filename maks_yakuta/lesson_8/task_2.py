"""
Создать 2 класса truck и car, которые являются наследниками auto. Класс
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

class Auto:
    """
    Class Auto
    this is a class describing a car
    """
    def __init__(self, brand, mark, age, color=None, weight=None):
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1


class Truck(Auto):
    """
    class Truck
    inherited class from class Auto
    """
    def __init__(self, brand, mark, age, max_load, color=None, weight=None):
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight
        self.max_load = max_load
    def move(self):
        print ('attention')
        super().move()

    def load(self):
        sleep(1)
        print('load')
        sleep(1)

class Car(Auto):
    """
    class Car
    inherited class from class Auto
    """
    def __init__(self, brand, mark, age, max_speed, color, weight):
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight
        self.max_speed = max_speed
    def move(self):
        print(f'max speed is {self.max_speed}')

truck_1 = Truck('Iveco','626i',5, 2500, 'Green', 3500)
truck_2 = Truck('Mercedes', 'Ivi', 6, 2000, 'Yellow', 3200)
car_1 = Car('BMW', 323, 5, 185, 'Black', 2100)
car_2 = Car('Audi', 'A8', 4, 256, 'White', 2400)
truck_1.move()
truck_2.move()
truck_1.load()
truck_2.load()
car_1.move()
car_2.move()


