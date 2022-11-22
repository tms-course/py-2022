import math
from math import sqrt


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """
        Method that counts distance from point object to point(0.0)
        :return: distance
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __repr__(self):
        return repr(f'Point object. x = {self.x}, y = {self.y}, distance from origin = {self.distance_from_origin()}')

    def __str__(self):
        return f'x = {self.x} y = {self.y}, distance from origin = {self.distance_from_origin()}'


class Circle(Point):
    def __init__(self, radius: int):
        super().__init__(radius, 0)
        self.radius = radius

    def edge_distance_from_origin(self):
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __sub__(self, other):
        """
        Subdivision of two Circles
        :param other: other Circle
        :return: origin point in case of equivalence of radiuses, else Circle with radius as subdivision result
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
        return self.radius == other.radius

    def __repr__(self):
        return repr(f'Circle object. Radius = {self.radius}')

    def __str__(self):
        return f'Radius = {self.radius}'


