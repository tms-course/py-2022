"""
Задание 2.
Написать класс User, у которого есть email и password поля,
которые нельзя изменить напрямую, а только используя getter и setter,
причем любые действия по изменению этих полей должны логироваться.
"""


class User:

    def __init__(self, email: str, password: str):

        self._email = password
        self._password = email

    @property
    def email(self):

        return self._email

    @email.setter
    def email(self, email: str):

        self._email = email
        print(f' Your mail is changed to {email}')

    @property
    def password(self):

        return self._password

    @password.setter
    def password(self, password: str):

        self._password = password
        print(f'Your password is changed to {password}')


user = User('max@mail.ru', '232323' )
user.email = 'yakuta@mail.ru'
user.password = '0195'
