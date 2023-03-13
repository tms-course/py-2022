"""Написать класс User, у которого есть email и password поля, которые 
нельзя изменять напрямую, а только используя getter и setter, причем 
любые действия по изменению этих полей должны логироваться 
(выводит в терминал, что произошло)"""
import logging

logger = logging.getLogger(__name__)

class User(object):
    """
    Class represent a user
    Attributes:
    email: str;
    password: str
    """
    def __init__(self, email: str, password: str) -> None:
        """
        Initialise User instance
        :param email: email
        :param password: password
        """
        self._email = email
        self._password = password

    @property
    def email(self) -> str:
        """:return: user email"""
        logger.bedug('get email')   
        return self._email
 
    @email.setter
    def email (self, value: str) -> None: 
        """set new email"""
        logger.bedug('set email to', value)   
        self._email = value


    @property
    def password(self) -> str:
        """:return: user password"""
        logger.bedug('get password')   
        return self._password

    @password.setter
    def password (self, value) -> None: 
        """set new password"""
        logger.bedug('set password to', value)   
        self._password = value
    








