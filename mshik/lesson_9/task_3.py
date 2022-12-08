"""
Задание 3.
Написать метакласс Registory, который будет отслеживать количество всех соданных
объектов класса Entry, в свою очередь класс Entry не должен содержать ничего,
связанного с логикой работы метакласса, кроме class Enrtry(metaclass=Registry).
"""
class Registory(type):
    """
    Metaclass to count new instances of classes
    Attributes:
        _instances_counter (int): int to count new instances of class Entry
    """
    _instances_counter = 0
        
    def __call__(cls, *args, **kwargs) -> None:
        """
        Magic metod increases count in _instances_counter, if new object created for class Entry.
        
        Attributes:
            cls (Registory): Registory class
            args (tuple): positional arguments
            kwargs (dict): keywoard arguments
        """
        class_name = cls.__name__
        if class_name == "Entry":
            Registory._instances_counter += 1
        return cls.__new__(cls, *args, **kwargs)


class Entry(metaclass=Registory):
    pass


for _ in range(5):
    print(Entry()) # <__main__.Entry object at ...>

print(Registory._instances_counter) # 5