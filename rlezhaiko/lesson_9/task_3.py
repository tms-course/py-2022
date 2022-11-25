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
    def __new__(cls, name, bases, attr) -> None:
        """ 
        __new__ function
        
        :param cls: cls
        :param name: name of class
        :param bases: parent of class
        :param attr: attr of class
        :returns: return None
        """
        attr['instances'] = attr.get('i', 0)
        return type.__new__(cls, name, bases, attr)
    
    
    def __call__(self) -> None:
        """ 
        __call__ function
        
        :param self: self
        :returns: return None
        """
        self.instances += 1
    

class Entry(metaclass=Registry):
    pass


for _ in range(100):
    _ = Entry()

print(Entry.__dict__)