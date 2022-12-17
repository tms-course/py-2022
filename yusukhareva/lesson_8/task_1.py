""" Класс авто с обязательными атрибутами бренд, возраст и марка, необязательными цвет и вес, 
с методами двигаться и стоять, 
и методом день рождения , кторый выдает на год больше

:param attrs: метод необязательных атрибутов
"""


class Auto ():
    def __init__(self , brand , age, mark ):
        self.brand = brand
        self.age = age
        self.mark = mark

    def attrs(self, colour, weight):
        self.colour = colour
        self.weight = weight


    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday (self, age):
        self.age = age
        age+=1
        print(age)

ford = Auto ('ford', 5, 'focus')
ford.birthday(5)
print (ford.__dict__)