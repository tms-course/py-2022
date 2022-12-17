"""
Создать родительский класс auto, у котторого есть атрибуты: brand, age, color, mark
и weight. А также методы: move, birthday и stop. Методы move и stop выводят
сообщение на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
Атрибуты brand, age, mark являются обязательными при объявлении объекта.
"""
import time


class Auto:
    def __init__(self, brand: str, mark: str, age: int, color: str = None, weight: int = None):
        """
        Init Auto object
        :param brand: auto's brand
        :param mark: auto's mark
        :param age: auto's age
        :param color: auto's color
        :param weight: auto's weight
        """
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
        print(self.age)



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


class Truck(Auto):
    def __init__(self, brand: str, mark: str, age: int, max_load: int, color: str = None, weight: int = None):
        """
        Init Truck object
        :param brand:
        :param mark:
        :param age:
        :param max_load:
        :param color:
        :param weight:
        """
        super().__init__(brand, mark, age, color, weight)
        self.max_load = max_load

    def move(self):
        print('attencion')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, mark: str, age: int, max_speed: int, color: str = None, weight: int = None):
        """
        Init Car object
        :param brand:
        :param mark:
        :param age:
        :param max_speed:
        :param color:
        :param weight:
        """
        super().__init__(brand, mark, age, color, weight)
        self.max_speed = max_speed

    def move(self):
        print(f'max speed is {self.max_speed}')
        super().move()


bmw_car = Auto('BMW', "X6", 1, 'black', 120)
jiguli_truck = Truck('Jiguli', '9', 40, 200, 'white', 700)
lada_car = Car('lada', 'sedan', 25, 500, 'grey', 170)
bmw_car.move()
bmw_car.birthday()
bmw_car.stop()
jiguli_truck.move()
jiguli_truck.load()
lada_car.move()
bmw_car.birthday()

