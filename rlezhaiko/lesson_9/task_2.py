""" 
2. #property #encapsulation
Написать класс User, у которого есть email и password поля, которые нельзя изменять
напрямую, а только используя getter и setter, причем любые действия по изменению
этих полей должны логироваться (выфводит в терминал, что произошло)
"""


class User(object):
    """
    Creates an instance of User class, where instance have email and password attribute
    """
    def __init__(self, email: str = '', password: str = '') -> None:
        """ 
        :param email: email
        :param password: password
        """
        self.__email = email
        self.__password = password
    

    def get_email(self) -> str:
        """
        :returns: return str
        """
        print('Getter email work...')
        return self.__email
    
    
    def set_email(self, email) -> None:
        """
        :param email: email of object
        """
        print('Setter email work...')
        self.__email = email
    
    
    def get_password(self) -> str:
        """
        :returns: return str
        """
        print('Getter password work...')
        return self.__password
    
    
    def set_password(self, password) -> None:
        """ 
        :param password: password of object
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