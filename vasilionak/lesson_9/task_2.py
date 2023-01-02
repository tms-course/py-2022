"""Написать класс User, у которого есть email и password поля, которые 
нельзя изменять напрямую, а только используя getter и setter, причем 
любые действия по изменению этих полей должны логироваться 
(выводит в терминал, что произошло)"""


class User(object):
    """
    Class 'User'
    Attributes:
    email: str;
    password: str
    """
    def __init__(self, email: str='', password: str='') -> None:
        """
        Initialise User instance
        :param email: email
        :param password: password
        """
        self.__email = email
        self.__password = password

   
       
    def get_email(self) -> str:
        """
        getter email
        """
        print('Getter email')
        return self.__email
        

    
    def set_email(self, email) -> None:
        """
        setter email
        """
        print('Setter email')
        self.__email = email
        


    
    def get_password(self) -> str:
        """
        getter password
        """
        print('getter password')
        return self.__password
        

    
    def set_password(self, password) -> None:
        """
        setter password
        """
        print('Setter password')
        self.__password = password
        

    email = property(get_email, set_email)
    password = property(get_password, set_password)


user = User()
print(user.__dict__)
user.set_email("vasilionak@mail.ru")
print(user.get_email())
user.set_password('65468484')
print(user.get_password())






