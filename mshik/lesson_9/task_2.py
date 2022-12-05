"""
Задание 2.

Написать класс User, у которого есть email и password поля,
которые нельзя изменить напрямую, а только используя getter и setter,
причем любые действия по изменению этих полей должны логироваться.
"""
class User:
    """
    A classed used to represent a User

    Attributes:
        email (str): An email of a user
        password (int): An password of a user

    Properties:
        email: Returns user email
        email.setter: Set up a new user email
        password: Returns user password
        password.setter: Set up a new user password  
    """
    def __init__(self, email: str, password: str) -> None:
        """
        Args:
            email (str): An email of a user
            password (int): An password of a user
        """
        self._email = email
        self._password = password
    
    @property
    def email(self) -> str:
        """Returns a user email."""
        print("Returning an email..")
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        """
        Set up a new user email.
        
        Args:
            email (str): A new user email
        """
        print("Setting up an email..")
        self._email = email
    
    @property
    def password(self) -> str:
        """Returns a user password."""
        print("Returning a password..")
        return self._password

    @password.setter
    def password(self, password: str) -> str:
        """
        Set up a new user password.
        
        Args:
            password (str): A new user password
        """
        print("Setting up a password..")
        self._password = password

        
user = User("mshik@gmail.com", "12344321")
print(user.email)
print(user.password)
user.email = "m_shik@gmail.com"
user.password = "123321"
print(user.email)
print(user.password)