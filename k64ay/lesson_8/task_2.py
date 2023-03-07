import time

from task_1 import Auto


class Truck(Auto):
    def __init__(
        self, 
        brand: str, 
        age: int, 
        mark: str,
        max_load: float,
        color: str = None, 
        weight: float = None
    ) -> None:
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self) -> None:
        print('attention')

        super().move()

    def load(self) -> None:
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(
        self, 
        brand: str, 
        age: int, 
        mark: str,
        max_speed: int,
        color: str = None, 
        weight: float = None
    ) -> None:
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self) -> None:
        super().move()
        print(f'max speed is {self.max_speed}')

truck1 = Truck('Mersedes', 10, 'Benz', 2300, 'black', 5900)