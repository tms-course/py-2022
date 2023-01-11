"""Написать метакласс Registry, который будет отслеживать количество всех созданных
объектов класса Entry, в свою очередь класс Entry не должен содержать ничего, свя-
занного с логикой работы метакласса, кроме class Entry(metaclass=Registry).

"""


class Registry(type):
    """ 
    Metaclass to make instance counter 
    Attributes:
        itertools.count
    """
    counter = 0

    def __call__(cls, *args, **kwargs) -> None:
        class_name = cls.__name__
        if class_name == "Entry":
            Registry.counter += 1
        return cls.__new__(cls, *args, **kwargs)


class Entry(metaclass=Registry):
    pass   


c = Entry()
b = Entry()
print(Registry.counter)
d = Entry()
e = Entry()
print(Registry.counter)