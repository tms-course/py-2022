"""
Создать родительский класс Auto, с атрибутами brand, age, color, mark, weight.
Методы: move, birthday, stop.
Move и stop выводят на экран сообщения "move" и "stop", а birthday увеличивает age на 1.
Атрибуты brand, age и mark обязательны при объявлении объекта.
Создать 2 класса truck и car, которые являются наследника класса auto. Класс truck имеет дополнительный
обязательный атрибут max_loadю Переопределенный метод move, перед поялвнием надпии move выводит attention
его реализацию сделать при помощи оператра super. А так же дополнительный метод load. при его вызове
происходит пауза 1 сек., затем выдается сообщение load и снова пауза 1 сек. Класс car имеет дополнительный
обязательный фтрибут max_spead и при вызове метода move после появления надписи moveдолжна появиться
надпись max_speed is <max_speed>. Создать по 2 объекта для каждого из классов и провреить все их методы и атрибуты
"""
import time


class Auto:
    """
    Base class auto
    Attributes:
    brand: str
    age: int
    mark: int
    color: str
    weight: int
    """

    def __init__(self, brand: str, age: int, mark: str, color: str = 'red', weight: int = 2000) -> None:
        """
        :param brand: brand of auto
        :param age: age of auto
        :param mark: mark of auto
        :param color: color of auto(default: red)
        :param weight: weight of auto(default: 2000)
        """

        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight

    def move(self) -> None:
        """
        Prints 'Move'
        """
        print('Move')

    def birthday(self) -> None:
        """
        Increases age by 1
        """
        self.age += 1

    def stop(self) -> None:
        """
        Prints 'Stop'
        """
        print('Stop')


car = Auto('Ford', 7, 'Focus')
car.birthday()
print(car.__dict__)


class Truck(Auto):
    """
    Inherited class Truck
    Attributes:
    brand: str
    age: int
    mark: str
    max_load: int
    color: str = 'blue'
    weight: int = 3000
    """

    def __init__(self, brand: str, age: int, mark: str, max_load: int, color: str = 'blue', weight: int = 3000):
        """
        :param brand: brand of truck
        :param age: age of truck
        :param mark: mark of truck
        :param max_load: max load of truck
        :param color: truck color(default: blue)
        :param weight: truck weight(default: 3000)
        """

        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        """
        Prints 'Attention' before printing 'Move'
        """
        print('Attention')
        super().move()

    def load(self):
        """
        Sleeps 1 second before and 1 second after printing 'load'
        """
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    """
    Inherited class Car
    Attributes:
    brand: str
    age: int
    mark: str
    max_speed: int
    color: str = 'black'
    weight: int = 1500
    """

    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = 'black', weight: int = 1500):
        """
        :param brand: brand of a car
        :param age: age of a car
        :param mark: mark of a car
        :param max_speed: max speed of a car
        :param color: car color(default: black)
        :param weight: car weight(default: 1500)
        """

        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        """
        Prints 'Move', then prints max speed of a car
        """
        super().move()
        print(f'Max speed {self.max_speed}')


ford_ranger = Truck('Ford', 2, 'Ranger', 1000)
ford_f350 = Truck('Ford', 6, 'F-350', 900)
kia_rio = Car('Kia', 10, 'Rio', 200)
mazda_6 = Car('Mazda', 8, '6', 220)

ford_ranger.move()
ford_ranger.load()
ford_ranger.birthday()
print(ford_ranger.__dict__)

kia_rio.move()
kia_rio.stop()
kia_rio.birthday()
print(kia_rio.__dict__)
