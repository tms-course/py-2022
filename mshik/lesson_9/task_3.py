"""
Задание 3.

Написать метакласс Registory, который будет отслеживать количество всех соданных
объектов класса Entry, в свою очередь класс Entry не должен содержать ничего,
связанного с логикой рабоыт метакласса, кроме class Enrtry(metaclass=Registry).
"""
from collections import defaultdict


class Registory(type):
    """
    Metaclass to count new instances of classes

    Attributes:
        _instances_counter (defaultdict): defaultdict to count new instances of classes
    """
    _instances_counter = defaultdict(int)

    def __call__(cls, *args, **kwargs):
        """
        Magic metod increases count in _instances_counter, if new object created.
        
        Attributes:
            cls (Registory): Registory class
            args (tuple): positional arguments
            kwargs (dict): keywoard arguments
        """
        class_name = cls.__name__
        cls._instances_counter[class_name] += 1
        return cls._instances_counter[class_name]


class Entry(metaclass=Registory):
    pass


for _ in range(5):
    print(Entry()) # 5 — Is a final number.