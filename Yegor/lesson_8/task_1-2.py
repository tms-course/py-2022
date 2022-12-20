"""
Создать родительский класс auto, у котторого есть атрибуты: brand, age, color, mark
и weight. А также методы: move, birthday и stop. Методы move и stop выводят
сообщение на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
Атрибуты brand, age, mark являются обязательными при объявлении объекта.
"""
import time


class Auto:
    """
    A classed used to represent an Auto
    Attributes:
        brand (str): Car brand
        age (int): An age of a Car
        mark (str): Car mark
        color (str): Car color
        weight (int): Gross Car weight
    Methods:
        move(): Prints move
        stop(): Print stop
        birthday(): Increases an age on 1
      """
    def __init__(self, brand: str, mark: str, age: int, color: str = None, weight: int = None):
        """
        Args:
            brand (str): Car brand
            age (int): An age of a car
            mark (str): Car mark
            color (str): Car color
            weight (int): Gross car weight
        """
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight

    def move(self):
        """
        prints 'move'
        :return: None
        """
        print('move')

    def stop(self):
        """
        prints 'stop'
        :return: None
        """
        print("stop")
        print('stop')

    def birthday(self):
        """
        Increases age on 1
        :return: None
        """
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
    """
    A classed used to represent a Truck.
    Truck class inherits from class Auto.
    Attributes:
        brand (str): Car brand
        age (int): An age of a car
        mark (str): Car mark
        max_load (int): Max load of a truck
        color (str): Car color
        weight (int): Gross car weight

    Methods:
        move(): Prints attention, then move
        load(): Waits for a sec, then prints load and after sleeps 1  sec
    """
    def __init__(self, brand: str, mark: str, age: int, max_load: int, color: str = None, weight: int = None):
        """
            Args:
                brand (str): Trucket brand
                age (int): An age of a truck
                mark (str): Truck mark
                max_load (int): Max load of a truck
                color (str): Truck color
                weight (int): Gross truck weight
        """
        super().__init__(brand, mark, age, color, weight)
        self.max_load = max_load

    def move(self):
        """
        Prints 'attention', then prints 'move'
        :return: None
        """
        print('attencion')
        super().move()

    def load(self):
        """
        Waits for a sec, then prints 'load' and waits for a second again
        :return: None
        """
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    """
        A classed used to represent a Car
        Car class inherits from class Auto.
        Attributes:
            brand (str): Car brand
            age (int): An age of a vehicle
            mark (str): Car mark
            max_speed (int): Max speed of a truck
            color (str): Car color
            weight (int): Gross car weight

        Methods:
            move(): Prints move, then max speed of a car
    """
    def __init__(self, brand: str, mark: str, age: int, max_speed: int, color: str = None, weight: int = None):
        """
            Args:
                brand (str): Car brand
                age (int): An age of a car
                mark (str): Car mark
                max_speed (int): Max speed of a car
                color (str): Car color
                weight (int): Gross car weight
        """
        super().__init__(brand, mark, age, color, weight)
        self.max_speed = max_speed

    def move(self):
        """
        Prints 'move' then prints max_speed
        :return: None
        """
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

