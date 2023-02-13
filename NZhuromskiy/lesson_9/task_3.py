"""
3.
Написать метакласс Registry, который будет отслеживать количество всех созданных объектов класса Entry,
в свою очередь класс Entry не должен содержать ничего, свя- занного с логикой работы метакласса,
кроме class Entry(metaclass=Registry).
"""


class Registry(type):
    """
    A class that keeps track of the number of all created objects of the Entry class.
    Class Attributes:
        _count_instance_class - we save it to the dictionary for counting new objects of the Entry class.
    """
    _count_instance_class = {}

    def __call__(cls, *args, **kwargs):
        """
        Dander method called when creating new objects, increasing their number.
        :param args:
        :param kwargs:
        :return:
        """
        name_class = cls.__name__
        cls._count_instance_class[name_class] = cls._count_instance_class.get(name_class, 0) + 1
        return cls.__new__(cls, *args, **kwargs)


class Entry(metaclass=Registry):
    pass


class Entry_2(metaclass=Registry):
    pass


class Entry_3(metaclass=Registry):
    pass


first_class = Entry()
second_class = Entry()
third_class = Entry_2()
fourth_class = Entry_3()

print(Registry._count_instance_class[Entry.__name__])
print(Registry._count_instance_class[Entry_2.__name__])
print(Registry._count_instance_class[Entry_3.__name__])




