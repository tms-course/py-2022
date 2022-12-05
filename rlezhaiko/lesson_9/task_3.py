""" 
3. #metaclass
Написать класс Registry, который будет отслеживать количество всех созданных
объектов класса Entry
"""

class Registry(type):
    """
    Metaclass counting all new instances
    """
    instances = 0
    def __new__(cls, name, bases, attr) -> None:
        """ 
        :param cls: cls
        :param name: name of class
        :param bases: parent of class
        :param attr: attr of class
        """
        return type.__new__(cls, name, bases, attr)
    
    
    def __call__(self) -> None:
        if self.__name__ == 'Entry':
            Registry.instances += 1
    

class Entry(metaclass=Registry):
    pass


for _ in range(100):
    _ = Entry()

print(Registry.__dict__)