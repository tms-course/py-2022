"""
2.
Написать класс User, у которого есть email и password поля, которые нельзя изменять напрямую,
а только используя getter и setter, причем любые действия по изменению этих полей
должны логироваться (выводит в терминал, что произошло)
"""


class User:
    """
    The class contains user fields.
    Class Attributes:
        fields email: user email
        fields password: user password
    """

    def __init__(self, email: str | None, password: str | None):
        """
        Initialise user instance
            :param str email: user email
            :param str password: user password
        """
        self._email = email
        self._password = password

    @property
    def email(self):
        """
        :return: user email
        """
        return self._email

    @property
    def password(self):
        """
        :return: user password
        """
        return self._password

    @email.setter
    def email(self, email: str):
        """
        Sets the email address
        :param str email: user email
        :return: None
        """
        self._email = email
        print(f"Email has been changed. New email: {email}")

    @password.setter
    def password(self, password: str):
        """
        Sets the password
        :param password: user password
        :return: None
        """
        self._password = password
        print(f"Password has been changed. New password: {password}")


user = User('asdada@mail.ru', 'asdasdad')
user.email = 'asdasasasasada@mail.ru'
user.password = 'asdasasasasasdad'
