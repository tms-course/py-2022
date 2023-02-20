"""
Создать родительский класс auto, у котторого есть атрибуты: brand, age, color, mark
и weight. А также методы: move, birthday и stop. Методы move и stop выводят
сообщение на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
Атрибуты brand, age, mark являются обязательными при объявлении объекта.
"""
class Auto:
    """
    Class Auto
    this is a class describing a car
    """
    def __init__(self, brand, mark, age, color=None, weight=None):
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight


    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1

car = Auto('Nissan', 'Qashqai', 21)
car.move()
car.stop()
car.birthday()

print(car.age)
