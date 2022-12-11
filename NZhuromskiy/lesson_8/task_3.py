from __future__ import annotations


class Point:
    """класс Point принимает в себя два атрибута x: float, y: float и метод __repr__()"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        """можно использовать ___str___(в определённых случаях удобнее читается)"""
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class Circle(Point):
    """класс Circle представляет собой окружность, он являтся подклассом и наследует от суперкласса Point,
    включает в себя методы __sub__(), __repr__()"""
    def __init__(self, center_x: float, center_y: float, radius: float):
        super().__init__(center_x, center_y)
        self.radius = radius

    def __sub__(self, deducted):
        """Будем возвращать Point при равности радиусов 1-й и 2-й окружностей, а если
        радиусы будут неравны то должна вернуться Circle"""
        x = self.x - deducted.x
        y = self.y - deducted.y
        if self.radius == deducted.radius:
            return Point(x, y)
        return Circle(x, y, abs(self.radius - deducted.radius))

    def __repr__(self):
        """можно использовать ___str___(в определённых случаях удобнее читается)"""
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.radius})"


circle_one = Circle(-6, 4, 5)
circle_two = Circle(-7, 5, 5)

print(circle_one, circle_two, circle_one - circle_two)
