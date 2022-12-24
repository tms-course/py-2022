"""
Для класса Circle реализовать метод производящий вычитание двух окружностей, вычитание радиусов произвести по модулю.
Если вычитаются две окружности с одинаковыми значением радиуса, то результатом вычитания будет точка класса Point.
"""
from math import sqrt, pi


class Point:
    """
    Base class Point
    Attributes:
    x: float
    y: float
    """

    def __init__(self, x: float, y: float):
        """
        Initialisation method
        :param x: point x
        :param y: point y
        """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """
        Prints distance from origin
        """
        print(sqrt(self.x ** 2 + self.y ** 2))

    def __eq__(self, other):
        """
        __eq__ function
        :param other:  other object of class
        :return: True if equals, False otherwise
        """
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        """
        __repr__ function
        :return: str
        """
        return f'First point x = {self.x}, second point y = {self.y}'

    def __str__(self):
        """
        __str__ function
        :return: str
        """
        return f'Point x = {self.x}, point y = {self.y}'


class Circle(Point):
    """
    Inherited class Circle
    Attributes:
    x: float
    y: float
    radius: float
    """

    def __init__(self, x: float, y: float, radius: float):
        """
        Initialisation method
        :param x: float
        :param y: float
        :param radius: radius of a circle
        """
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        """
        __eq__ function
        :param other: other object of class
        :return: True if equal, False otherwise
        """
        return (self.x == other.x) and (self.y == other.y) and (self.radius == other.radius)

    def __repr__(self):
        """
        __repr__ function
        :return: str
        """
        return f'First point x = {self.x}, second point y = {self.y}, and radius = {self.radius}'

    def __str__(self):
        """
        __str__ function
        :return: str
        """
        return f'Point x = {self.x}, point y = {self.y}, radius = {self.radius}'

    def edge_distance_from_origin(self):
        """
        :return: Circle radius
        """
        return self.radius

    def area(self):
        """
        area function
        :return: area of a circle
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
        :param other: other object of class
        :return: Point, if radius of both circle are the same, otherwise Circle
        """
        x = self.x - other.x
        y = self.y - other.y
        if self.radius == other.radius:
            return Point(x, y)
        return Circle(x, y, abs(self.radius - other.radius))


circle_1 = Circle(-4, 2, 2)
circle_2 = Circle(-3, 1, 2)
print(circle_1)
print(circle_2)
print(circle_1 - circle_2)
