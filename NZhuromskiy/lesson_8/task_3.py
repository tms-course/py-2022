from __future__ import annotations


class Point:
    """
    Class used for represent a point
    Class Attributes:
    x: float
    y: float
    """
    def __init__(self, x: float, y: float):
        """
        :param x: point x
        :param y: point y
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """Formal representation of the object"""
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class Circle(Point):
    """
    Heir from the Point class;
    Class Attributes:
        center_x: float
        center_y: float
        radius: float
    """
    def __init__(self, center_x: float, center_y: float, radius: float):
        """
        :param center_x: central point x
        :param center_y: central point y
        :param radius: circle radius
        """
        super().__init__(center_x, center_y)
        self.radius = radius

    def __sub__(self, deducted):
        """We will return Point if the radii of the 1st and 2nd circles are equal, and if
        the radii are unequal, then Circle should return"""
        x = self.x - deducted.x
        y = self.y - deducted.y
        if self.radius == deducted.radius:
            return Point(x, y)
        return Circle(x, y, abs(self.radius - deducted.radius))

    def __repr__(self):
        """Formal representation of the object"""
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.radius})"


circle_one = Circle(-6, 4, 5)
circle_two = Circle(-7, 5, 5)

print(circle_one, circle_two, circle_one - circle_two)
