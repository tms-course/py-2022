"""Создат родител ски класс auto, у которого есть атрибуты: brand, age, cоlor, mark,
и weight. А так же методы:move, birthday, stop. Методы move и sop выводят сообщение
 на экран "move" "stop", birthday увеличивает атрибут age на 1. Атрибуты brand, age,
 mark являются обязательными при объявлении объекта"""

class Auto:
    def __init__(self, brand: str, age: int, mark: int, color: str = None, weight: float = None) -> None:
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        print(self.age + 1)

jacket = Auto('Audi', 5, 5)
jacket.birthday()
print(jacket.__dict__)


