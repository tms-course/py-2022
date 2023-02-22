"""
Задание 2.
Написать класс User, у которого есть email и password поля,
которые нельзя изменить напрямую, а только используя getter и setter,
причем любые действия по изменению этих полей должны логироваться.
"""


class User:
    """
    Class represents user
    Attributes:
        string email: user's email
        string password: user's password
    """
    def __init__(self, email: str | None, password: str | None):
        """
        Initialise user instance
        :param str email: user's email (optionally)
        :param str password: user's password (optionally)
        """
        self._email = password
        self._password = email

    @property
    def email(self):
        """
        :return: user's email
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """
        Sets user email
        :param email: user's email
        :return: None
        """
        self._email = email
        print(f'Email was changed. Your email is {email}')

    @property
    def password(self):
        """
        :return: user's password
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """
        Sets user's password
        :param password: none
        :return:
        """
        self._password = password
        print(f'Password was changed. Your password is {password}')


user = User()
user.email = 'denis@cekfdmcdkm'
user.password = '1111111111'
user.email = 'denis@gmail.com'
user.password = 'qwerty09876'
