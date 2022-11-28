"""Создать 2 класса truck и car, которые являются наследника класса auto. Класс truck имеет дополнительный
обязательный атрибут max_loadю Переопределенный метод move, перед поялвнием надпии move выводит attention
его реализацию сделать при помощи оператра super. А так же дополнительный метод load. при его вызове
происходит пауза 1 сек., затем выдается сообщение load и снова пауза 1 сек. Класс car имеет дополнительный
обязательный фтрибут max_spead и при вызове метода move после появления надписи moveдолжна появиться
надпись max_speed is <max_speed>. Создать по 2 объекта для каждого из классов и провреить все их методы и атрибуты"""


import time


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = None, weight: float = None) -> None:
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        print(self.age + 1)


class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_load: float, color: str = None, weight: float = None) -> None:
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('Atention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = None, weight: float = None) -> None:
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
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



