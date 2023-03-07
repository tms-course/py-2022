class Registry(type):
    _obj_count = 0

    def __call__(self):
        if self is Entry:
            Registry._obj_count += 1

        return super().__call__()


class Entry(metaclass=Registry):
    def __init__(self) -> None:
        self.x = 10


entry1 = Entry()
entry2 = Entry()



print(Registry._obj_count)