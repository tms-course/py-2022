#ДОДЕЛАТЬ

class Circle:
    def __init__(self, len_circle, radius):
        self.len_circle = len_circle
        self.radius = radius
        len_circle = 2*3.14*radius

    def __sub__(self, len_circle):
        self.len_circle = len_circle
        return Circle(self.value - len_circle.value)

    def __sub__(self, radius):
        self.radius = radius
        return Circle(abs(self.value - radius.value))

circle1 = Circle(31.4 , 5)
circle2 = Circle(62.8, 10)
c = circle1 - circle2