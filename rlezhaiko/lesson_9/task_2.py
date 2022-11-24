""" 
2. #property #encapsulation
Написать класс User, у которого есть email и password поля, которые нельзя изменять
напрямую, а только используя getter и setter, причем любые действия по изменению
этих полей должны логироваться (выфводит в терминал, что произошло)
"""

class User(object):
    def __init__(self, email: str = '', password: str = '') -> None:
        """ 
        __init__ function
        
        :param self: self object of class
        :param email: email
        :param password: password
        :returns: return None
        """
        self.__email = email
        self.__password = password
    

    def get_user(self) -> str:
        """ 
        Getter function
        
        :param self: self object of class
        :returns: return str
        """
        print('Getter work...')
        return f'{self.__email} {self.__password}'
    
    
    def set_user(self, email, password) -> None:
        """ 
        Setter function
        
        :param self: self object of class
        :param email: email of object
        :param password: password of object
        :returns: return None
        """
        print('Setter work...')
        self.__email = email
        self.__password = password
    
    
    user_property = property(get_user, set_user)
    

a = User()
print(a.__dict__)
a.set_user('example@gmail.com', '1234567')
print(a.get_user())