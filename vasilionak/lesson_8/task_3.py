"""Для класса Circle реализовать метод производящий вычитание двух окружностейб вычитание радиусов произвести по модулю
Если вычитаются две окружности с одинаковыми значением радиуса, то результатом вычитания будет точка класса Point"""
from math import sqrt, pi


class Point:
    """
    Class Point
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
        Print distance from origin
        """
        print(sqrt(self.x ** 2 + self.y ** 2))

    def __repr__(self):
        """
        __repr__ function
        :return: Returns a string as a representation of the object
        """
        return f'First point x = {self.x}, second point y = {self.y}'

    def __str__(self):
        """
        __str__ function
        :return str
        """
        return f'Point x = {self.x}, point y = {self.y}'

    def __eq__(self, other):
        """
        __eq__ function
        :param other:  other object of class
        :return: return True if equals, False otherwise
        """
        return (self.x == other.x) and (self.y == other.y)

class Circle(Point):
    """
    Class that represents a circle
        Attributes:
            x: float
            y: float
            radius: float
    """
    def __init__(self, x: float, y: float, radius: float):
        """
        Initialisation of Circle object
        :param x: float
        :param y: float
        :param radius: float
        """
        super(self).__init__(x, y)
        self.radius = radius


    def __repr__(self):
        """
        __repr__ function
        :return: Returns a string as a representation of the object
        """
        return f'First point x = {self.x}, second point y = {self.y}, and radius = {self.radius}'

    def __str__(self):
        """
        __str__ function
        :return str
        """
        return f'Point x = {self.x}, point y = {self.y}, radius = {self.radius}'

    def __eq__(self, other):
        """
        __eq__ function
        :param other:  other object of class
        :return: return True if equals, False otherwise
        """
        return (self.x == other.x) and (self.y == other.y) and (self.radius == other.radius)


    def area(self):
        """
        area function
        :return: area of circle
        """
        return pi * self.radius ** 2

    def circumference(self):
        """
        circumference function
        :return: circumference
        """
        return 2 * pi * self.radius

    def __sub__(self, other):
        """
        __sub__ function
        :param self object
        :param other: other object
        :return: Point, if radius of both circle are the same, if not: Circle with radius as subtracting result
        """
        x = self.x - other.x
        y = self.y - other.y
        if self.radius == other.radius:
            return Point(x, y)
        return Circle(x, y, abs(self.radius - other.radius))


