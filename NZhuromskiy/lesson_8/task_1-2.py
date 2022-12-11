import time


class Auto:

    def __init__(self, brand, age: int, mark, color: str = None, weight: int = None):
        self.age = age
        self.brand = brand
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        """Вывод ссобщения Move"""
        print('move')

    def stop(self):
        """Вывод сообщения Stop"""
        print('stop')

    def birthday(self):
        """Увеличивает атрибут age на 1"""
        self.age += 1


class Truck(Auto):

    def __init__(self, brand, age: int, max_load, mark, color: str = None, weight: int = None):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        """Выводит Attention перед move"""
        print('attention')
        super().move()

    def load(self):
        """При вызове пауза 1 сек, потом вывод текста load, затем опять пауза 1 сек"""
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):

    def __init__(self, brand, age: int, max_speed: float, mark, color: str = None, weight: int = None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        """после надписи move появляется надпись max_speed is <max_speed>"""
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
