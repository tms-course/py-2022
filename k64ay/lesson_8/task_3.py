from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, another: 'Point') -> bool:
        return self.x == another.x and self.y == another.y
    

class Circle(Point):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, another: 'Circle') -> bool:
        return self.radius == another.radius and super().__eq__(another)

    def __sub__(self, another: 'Circle') -> 'Circle' | Point:
        new_x = self.x - another.x
        new_y = self.y - another.y
        new_radius = abs(self.radius - another.radius)

        if not new_radius:
            return Point(new_x, new_y)
        
        return Circle(new_x, new_y, new_radius)