"""
Задание 3.
Написать метакласс Registory, который будет отслеживать количество всех соданных
объектов класса Entry, в свою очередь класс Entry не должен содержать ничего,
связанного с логикой рабоыт метакласса, кроме class Enrtry(metaclass=Registry).
"""


class Registry(type):
    """
    Metaclass to count new instances of classes
    Attributes:
        dictionary_for_instances_amount (defaultdict): defaultdict to count new instances of classes
    """
    dictionary_for_instances_amount = dict()

    def __call__(cls, *args, **kwargs):
        """
        Magic method called when new objects are created and increases their count
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return:
        """
        class_name = cls.__name__
        cls.dictionary_for_instances_amount[class_name] = cls.dictionary_for_instances_amount.get(class_name, 0) + 1
        return cls.dictionary_for_instances_amount[class_name]


class Instance(metaclass=Registry):
    pass

first = Instance()
second = Instance()
print(second)
