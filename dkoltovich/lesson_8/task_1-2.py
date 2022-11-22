import time


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = 'black', weight: int = 500):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Truck(Auto):

    def __init__(self, brand: str, age: int, mark: str, max_load: int, color='black', weigth=500):
        super().__init__(brand, age, mark, color, weigth)
        self.max_load = max_load

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color='black', weigth=500):
        super().__init__(brand, age, mark, color, weigth)
        self.max_speed = max_speed

    def move(self):
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
