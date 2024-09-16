""" Класс авто с обязательными атрибутами бренд, возраст и марка, необязательными цвет и вес, 
с методами двигаться и стоять, 
и методом день рождения , кторый выдает на год больше

Класс truck с добавлением максимальной загрузкой и методом , выводящим через секунду load
Класс car с добавлением вывода максимальной скорости 

:param attrs: метод необязательных атрибутов
"""
import time

class Auto ():
    def __init__(self , brand , age, mark ):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')

    def stop(self):
        print('stop')


class Truck(Auto):
    def __init__(self , brand , age, mark, max_load):
        super().__init__( brand , age, mark)
        self.max_load = max_load

    def move(self):
        print('Attention!')
        super().move()
    
    def load(self):
        time.sleep (1)
        print ("load")
        time.sleep (1)

class Car(Auto):
    def __init__(self , brand , age, mark, max_speed):
        super().__init__( brand , age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print ('max speed is ', self.max_speed)




ford = Truck ('ford', 5, 'focus', 7)
print (ford.__dict__)
ford.move()
ford.load()


bmw = Car ('bmw', 2, 'x6', 200)
print (bmw.__dict__)
bmw.move()
