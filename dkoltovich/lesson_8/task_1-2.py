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
        color: str = 'black'
        weight: int = 500
    """
    def __init__(self, brand: str, age: int, mark: str, color: str = 'black', weight: int = 500):
        """
        Initialisation of Auto object
        :param brand: Auto's brand
        :param age: Auto's age
        :param mark: Auto's mark
        :param color: Auto's color, black by default
        :param weight: Auto's weight, 500 by default
        """
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        """
        prints 'move'
        :return: None
        """
        print("move")

    def stop(self):
        """
        prints 'stop'
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
           color: str = 'black'
           weight: int = 500
           max_load: int
       """

    def __init__(self, brand: str, age: int, mark: str, max_load: int, color='black', weigth=500):
        """
        Init Truck object
        :param brand:
        :param age:
        :param mark:
        :param max_load:
        :param color:
        :param weigth:
        """
        super().__init__(brand, age, mark, color, weigth)
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
           color: str = 'black'
           weight: int = 500
           max_speed: int
    """

    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color='black', weigth=500):
        """
        Init Car object
        :param brand:
        :param age:
        :param mark:
        :param max_speed:
        :param color:
        :param weigth:
        """
        super().__init__(brand, age, mark, color, weigth)
        self.max_speed = max_speed

    def move(self):
        """
        Prints 'move' then prints max_speed
        :return: None
        """
        super().move()
        print(f'Max speed is {self.max_speed}')


bmw_car = Car('BWM', 4, "X5", 120)
porsche_cer = Car('Porsche', 8, 'Cayenne', 200, 'red', 700)
yaz_truck = Truck('YAZ', 25, 'yaz', 2000)
maz_truck = Truck('MAZ', 9, 'maz-9', 10000, 'yellow')
bmw_car.move()
porsche_cer.move()
maz_truck.load()
maz_truck.move()
yaz_truck.birthday()
print(yaz_truck.get_age())
