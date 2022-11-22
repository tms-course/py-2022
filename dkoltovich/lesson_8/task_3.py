"""
task 3:
Реализовать для класса Circle, рассмотренного на уроке, метод вычитания окружностей.
Если радиусы окружностей равны, то вернуть объект класса Point

"""

import math
from math import sqrt


class Point:
    """
    Class that represents a Point
    Attributes:
        x: float
        y: float
    """
    def __init__(self, x: float, y: float):
        """
        Initialisation of Point object
        :param x: coordinate x
        :param y: coordinate y
        """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """
        Method that counts distance from point object to point(0.0)
        :return: distance
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        """
        comparison of Points
        :param other: other Point to compare
        :return: True if points are equal, False otherwise
        """
        return other.x == self.x and other.y == self.y


class Circle(Point):
    """
    Class that represents a circle
    Attributes:
        x: float
        y: float
        radius: float
    """
    def __init__(self, radius: int):
        """Initialisation of Circle object
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
        """
        Calculates the aria of the circle
        :return: area
        """
        return math.pi * self.radius ** 2

    def __sub__(self, other):
        """
        Subtracting of two Circles
        :param other: other Circle
        :return: origin point in case of equivalence of radiuses, else Circle with radius as subtracting result
        """
        if self.radius == other.radius:
            return Point(0, 0)

        return Circle(abs(self.radius - other.radius))

    def circumference(self):
        """
        Counts the length of circle's line
        :return: the length
        """
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        """
        comparison of two circles
       :param other:  Circle to compare
       :return: True if circles are equal, False otherwise
        """
        return self.radius == other.radius

