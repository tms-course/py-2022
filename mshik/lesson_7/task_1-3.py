from __future__ import annotations

import time


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = None, weight: float = None) -> None:
        """
        Args:
            brand (str): Car brand
            age (int): The age of a vehicle
            mark (str): Vehincle mark
            color (str): Vehincle color
            weight (str): Gross vehicle weight
        """
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
    
    def move(self) -> None:
        print("move")
    
    def stop(self) -> None:
        print("stop")
    
    def birthday(self) -> None:
        """Increases the age by one"""
        self.age += 1


class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_load: float, color: str = None, weight: float = None) -> None:
        """
        Args:
            brand (str): Trucket brand
            age (int): The age of a truck
            mark (str): Truck mark
            max_load (float): Max load of a truck
            color (str): Truck color
            weight (str): Gross truck weight
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load
    
    def move(self) -> None:
        print("attention")
        super().move()
    
    def load(self) -> None:
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: float, color: str = None, weight: float = None) -> None:
        """
        Args:
            brand (str): Car brand
            age (int): The age of a car
            mark (str): Car mark
            max_speed (float): Max speed of a car
            color (str): Car color
            weight (str): Gross car weight
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed
    
    def move(self) -> None:
        super().move()
        print(f"max speed is {self.max_speed}")


toyota_tundra = Truck("Toyota", 3, "Tundra", 1220.2, "White", 249.2)
ford_f150 = Truck("Ford", 5, "F150", 1233.3)
mercedes_e63s = Car("Mercedes Benz", 1, "E63s", 312.5, "Black", 123.3)
tesla_plaid = Car("Tesla", 1, "Plaid", 320)


# All methods and attributes of Truck instance
toyota_tundra.move()
toyota_tundra.load()
toyota_tundra.birthday()
print(toyota_tundra.brand, toyota_tundra.age, toyota_tundra.mark, toyota_tundra.max_load, toyota_tundra.color, toyota_tundra.weight)

# All methods and attributes of Car instance.
tesla_plaid.move()
tesla_plaid.stop()
tesla_plaid.birthday()
print(tesla_plaid.brand, tesla_plaid.age, tesla_plaid.mark, tesla_plaid.max_speed, tesla_plaid.color, tesla_plaid.weight)


class Point:
    def __init__(self, x: float, y: float) -> None:
        """
        Args:
            x (float): Point x
            y (float): Point y
        """
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    
class Circle(Point):
    def __init__(self, center_x: float, center_y: float, radius: float) -> None:
        """
        Args:
            center_x (float): Point center_x
            center_y (float): Point center_y
            radius (float): The radius of Circle
        """
        super().__init__(center_x, center_y)
        self.radius = radius

    def __sub__(self, other: Circle) -> Circle | Point:
        """Substract circles
        Args:
            other (Circle): Circle to substract
        Returns:
            obj (Circle | Point): Returns Point, if radius of both circle are the same, otherwise Circle
        """
        x = self.x - other.x
        y = self.y - other.y
        if self.radius == other.radius:
            return Point(x, y)
        return Circle(x, y, abs(self.radius - other.radius))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.radius})"


first_circle = Circle(-2, 2, 2)
print(first_circle) # Circle (-2, 2, 2)
second_circle = Circle(-3, 3, 2)
print(second_circle) # Circle (-3, 3, 2)
print(first_circle - second_circle) # Point(1, -1)