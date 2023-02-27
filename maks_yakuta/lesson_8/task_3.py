"""
3. *Для рассмотренного на уроке класса Circle реализовать метод производящий
вычитание двух окружностей, вычитание радиусов произвести по модулю. Если
вычитаются две окружности с одинаковым значением радиуса, то рузультатом
вычитания будет точка класса Point.
"""
from math import sqrt, pi


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        return f'First point x = {self.x}, second point y = {self.y}'

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle(Point):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return f'First point x = {self.x}, second point y = {self.y}, and radius = {self.radius}'

    def __str__(self):
        return f'Point x = {self.x}, point y = {self.y}, radius = {self.radius}'

    def edge_distance_from_origin(self):
        return self.radius

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        if self.radius == other.radius:
            return Point(x, y)
        return Circle(x, y, abs(self.radius - other.radius))

circle_1 = Circle(2,3,5)
circle_2 = Circle(2,3,5)
print(circle_1.area())
print(circle_1.circumference())
print(circle_1.edge_distance_from_origin())
print(circle_1 == circle_2)
p = Point(3,2)
p1 = Point(2,3)
print(p == p1)



