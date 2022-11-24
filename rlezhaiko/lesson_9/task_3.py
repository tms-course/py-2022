""" 
3. #metaclass
Написать класс Registry, который будет отслеживать количество всех созданных
объектов класса Entry
"""

class Registry(type):
    """
    Class Registry
    
    Metaclass fixed all new instances
    """
    instances = 0
    def __new__(cls, name, bases, attr):
        """ 
        __new__ function
        
        :param cls: cls
        :param name: name of class
        :param bases: parent of class
        :param attr: attr of class
        :returns: return None
        """
        return type.__new__(cls, name, bases, attr)


class Entry(metaclass=Registry):
    """
    Class Entry
    
    Creates an instance of a Entry class
    """
    def __init__(self) -> None:
        """ 
        __init__ function
        
        :param self: self object of class
        :returns: return None
        """
        Registry.instances += 1


for _ in range(100):
    _ = Entry()

print(Registry.instances)