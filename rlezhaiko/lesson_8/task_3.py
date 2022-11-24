"""
3. *Для рассмотренного на уроке класса Circle реализовать метод производящий
вычитание двух окружностей, вычитание радиусов произвести по модулю. Если
вычитаются две окружности с одинаковым значением радиуса, то рузультатом 
вычитания будет точка класса Point.
"""
from __future__ import annotations
from math import sqrt, pi


class Point(object):
    """
    Class Point
    
    Creates an instance of a Point class
    """
    def __init__(self, x: float, y: float) -> None:
        """
        __init__ function
        
        :param self: self object of class
        :param x: x of point
        :param y: y of point
        :returns: return None
        """
        self.x = x
        self.y = y


    def __repr__(self) -> str:
        """
        __repr__ function
        
        :param self: self object of class
        :returns: return str
        """
        return f'Point (x = {self.x}, y = {self.y})'
    
    
    def __str__(self) -> str:
        """
        __str__ function
        
        :param self: self object of class
        :returns: return str
        """
        return f'Point x is {self.x}, y is {self.y}'
    
    
    def __eq__(self, other: Point) -> bool:
        """
        __eq__ function
        
        :param self: self object of class
        :param other: other object of class 
        :returns: return True if equals, False otherwise
        """
        return (self.x == other.x) and (self.y == other.y)
    
    
    def distance_from_origin(self) -> float:
        """
        Distance from origin function
        
        :param self: self object of class 
        :returns: return float value from point to origin
        """
        return sqrt(self.x ** 2 + self.y ** 2)


class Circle(Point):
    """
    Class Circle
    
    Creates an instance of a Circle class
    """
    def __init__(self, x: float, y: float, radius: float) -> None:
        """
        __init__ function
        
        :param self: self object of class
        :param x: x of circle
        :param y: y of circle
        :param radius: radius of circle
        :returns: return None
        """
        super().__init__(x, y)
        self.radius = radius
    
    
    def __repr__(self) -> str:
        """
        __repr__ function
        
        :param self: self object of class
        :returns: return str
        """
        return f'Circle (x = {self.x}, y = {self.y}, radius = {self.radius})'
    
    
    def __str__(self) -> str:
        """
        __str__ function
        
        :param self: self object of class
        :returns: return str
        """
        return f'Circle x is {self.x}, y is {self.y}, radius is {self.radius}'
    
    
    def __eq__(self, other: Circle) -> bool:
        """
        __eq__ function
        
        :param self: self object of class
        :param other: other object of class 
        :returns: return True if equals, False otherwise
        """
        return (self.x == other.x) and (self.y == other.y) and (self.radius == other.radius)
    
    
    def __sub__(self, other: Circle) -> Circle | Point:
        """
        __sub__ function
        
        :param self: self object of class
        :param other: other object of class 
        :returns: return Circle or Point
        """
        x = self.x - other.x
        y = self.y - other.y
        difference = abs(self.radius - other.radius)
        if difference == 0:
            return Point(x, y)
        return Circle(x, y, difference)
    
    
    def edge_distance_from_origin(self) -> float:
        """
        Edge distance from origin function
        
        :param self: self object of class 
        :returns: return float value of edge distance from origin
        """
        distance_to_origin = super().distance_from_origin()
        return distance_to_origin + self.radius
    
    
    def area(self) -> float:
        """
        Area function
        
        :param self: self object of class 
        :returns: return float value of circle area
        """
        return pi * self.radius ** 2
    
    
    def circumference(self) -> float:
        """
        Circumference function
        
        :param self: self object of class 
        :returns: return float value of circumference
        """
        return 2 * pi * self.radius