class Registry(type):

    counter = 0

    def __call__(cls, *args, **kwargs) -> None:
        class_name = cls.__name__
        if class_name == "Entry":
            Registry.counter += 1
        return cls.__new__(cls, *args, **kwargs)


class Entry(metaclass=Registry):
    pass

class Counter(metaclass=Registry):
    pass

class_0 = Counter()
class_1 = Entry()
class_2 = Entry()
print(Registry.counter)
