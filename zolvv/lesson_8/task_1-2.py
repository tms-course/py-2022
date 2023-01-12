"""
task1-2:
Создать родительский класс Auto с методами move, stop birthday, и унаследовать от него классы Truck, Car.
Переопределить методы. В класс Truck добавить метод load
"""
import time
class Auto:
    """
    Base class auto
    Attributes:
        brand: str
        age: int
        mark: str
        color: str = 'mate-black'
        weight: int = 1000
    """
    def __init__(self, brand: str, age: int, mark: str, color: str = 'mate-black', weight: int = 1000):
        """
        Initialisation of Auto object
        :param brand: Auto's brand
        :param age: Auto's age
        :param mark: Auto's mark
        :param color: Auto's color, mate-black by default
        :param weight: Auto's weight, 1000 by default
        """
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        """
        print 'move'
        :return: None
        """
        print("move")

    def stop(self):
        """
        print 'stop'
        :return: None
        """
        print("stop")

    def birthday(self):
        """
        Increases age on 1
        :return: None
        """
        self.age += 1

    def get_age(self):
        """
        Getter method
        :return: Auto's age
        """
        return self.age


class Truck(Auto):
    """
       Inherited class Truck
       Attributes:
           brand: str
           age: int
           mark: str
           color: str = 'mate-black'
           weight: int = 1000
           max_load: int
       """

    def __init__(self, brand: str, age: int, mark: str, max_load: int, color='mate-black', weight=1000):
        """
        Init Truck object
        :param brand:
        :param age:
        :param mark:
        :param max_load:
        :param color:
        :param weight:
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        """
        Prints 'attention', then prints 'move'
        :return: None
        """
        print('Attention')
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
    Inherited class Truck
       Attributes:
           brand: str
           age: int
           mark: str
           color: str = 'mate-black'
           weight: int = 1000
           max_speed: int
    """

    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color='mate-black', weight=1000):
        """
        Init Car object
        :param brand:
        :param age:
        :param mark:
        :param max_speed:
        :param color:
        :param weight:
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        """
        Prints 'move' then prints max_speed
        :return: None
        """
        super().move()
        print(f'Max speed is {self.max_speed}')


mersedes_car = Car('Mersedes', 4, "S63-AMG", 150)
porsche_car = Car('Porsche', 8, 'Panamera', 200, 'white', 700)
ural_truck = Truck('URAL', 24, 'URAL-9', 2000)
maz_truck = Truck('MAZ', 9, 'maz-9', 10000, 'yellow')
mersedes_car.move()
porsche_car.move()
maz_truck.load()
maz_truck.move()
ural_truck.birthday()
print(ural_truck.get_age())