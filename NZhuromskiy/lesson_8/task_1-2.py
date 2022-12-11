import time


class Auto:
    """
    General class for cars
    Class Attributes:
        brand
        age: int
        mark
        color: str = None
        weight: int = None
    """
    def __init__(self, brand, age: int, mark, color: str = None, weight: int = None):
        """
        :param brand: car brand
        :param age: age of the car
        :param mark: car mark
        :param color: car color
        :param weight: car weight
        """
        self.age = age
        self.brand = brand
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        """Message output Move"""
        print('move')

    def stop(self):
        """Message output Stop"""
        print('stop')

    def birthday(self):
        """Increase the value of the age attribute by 1"""
        self.age += 1


class Truck(Auto):
    """
    Class used for represent a Truck
    Heir from the Auto class;
    Class Attributes:
        brand
        age: int
        max_load: float
        mark
        color: str = None
        weight: int = None
    """
    def __init__(self, brand, age: int, max_load: float, mark, color: str = None, weight: int = None):
        """
        :param brand: car brand
        :param age: age of the car
        :param max_load: maximum load of the truck
        :param mark: car mark
        :param color: car color
        :param weight: car weight
        """
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        """Outputs attention before move"""
        print('attention')
        super().move()

    def load(self):
        """When called, pause for 1 sec, then output the text load, and then pause again for 1 sec"""
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    """
    Class used for represent a Car
    Heir from the Auto class;
    Class Attributes:
        brand
        age: int
        max_speed: float
        mark
        color: str = None
        weight: int = None
    """
    def __init__(self, brand, age: int, max_speed: float, mark, color: str = None, weight: int = None):
        """
        :param brand: car brand
        :param age: age of the car
        :param max_speed: maximum speed of the car
        :param mark: car mark
        :param color: car color
        :param weight: car weight
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        """After the move message, the text max_speed is <max_speed> will appear"""
        super().move()
        print(f'max_speed is {self.max_speed}')


mercedes_benz = Truck('mercedes', 2, 3250, 'GLS', 'black', 2490)
ferrari = Truck('ferrari', 1, 2600, '812', 'white')
audi = Car('audi', 3, 238.5, 'Q8', 'mate-grey', 2540)
bmw = Car('bmw', 4, 225, '7-series')

mercedes_benz.move()
mercedes_benz.stop()
mercedes_benz.load()
mercedes_benz.birthday()
print(mercedes_benz.brand, mercedes_benz.age, mercedes_benz.max_load, mercedes_benz.mark, mercedes_benz.color,
      mercedes_benz.weight)

audi.move()
audi.stop()
audi.birthday()
print(mercedes_benz.brand, mercedes_benz.age, mercedes_benz.max_load, mercedes_benz.mark, mercedes_benz.color,
      mercedes_benz.weight)
