"""
task 3:
"Для класса Circle реализовать метод производящий вычитание двух окружностейб вычитание радиусов произвести по модулю
Если вычитаются две окружности с одинаковыми значением радиуса, то результатом вычитания будет точка класса Point
"""
import math
from math import sqrt


class Point:
    def __init__(self, x: float, y: float):
        """
        Init of Point objects
        :param x: coordinate x
        :param y: coordinate y
        """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


class Circle(Point):

    def __init__(self, radius: int):
        """Init of Circle object
        :param radius: radius of the circle
        """
        super().__init__(radius, 0)
        self.radius = radius

    def edge_distance_from_origin(self):
        """
        :return: Circle radius
        """
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __sub__(self, other):
        if self.radius == other.radius:
            return Point(0, 0)

        return Circle(abs(self.radius - other.radius))

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius