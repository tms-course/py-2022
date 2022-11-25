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
    

    def get_email(self) -> str:
        """ 
        Get email function
        
        :param self: self object of class
        :returns: return str
        """
        print('Getter email work...')
        return f'{self.__email}'
    
    
    def set_email(self, email) -> None:
        """ 
        Set email function
        
        :param self: self object of class
        :param email: email of object
        :returns: return None
        """
        print('Setter email work...')
        self.__email = email
    
    
    def get_password(self) -> str:
        """ 
        Get password function
        
        :param self: self object of class
        :returns: return str
        """
        print('Getter password work...')
        return f'{self.__password}'
    
    
    def set_password(self, password) -> None:
        """ 
        Set password function
        
        :param self: self object of class
        :param password: password of object
        :returns: return None
        """
        print('Setter password work...')
        self.__password = password
    
    
    email = property(get_email, set_email)
    password = property(get_password, set_password)
    

a = User()
print(a.__dict__)
a.set_email('example@gmail.com')
print(a.get_email())
a.set_password('1234567')
print(a.get_password())

a.email = '222example@gmail.com'
print(a.email)
a.password = '987654321'
print(a.password)