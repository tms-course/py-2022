import logging

logger = logging.getLogger(__name__)


class User:
    def __init__(self, email: str, password: str) -> None:
        self._email = email
        self._password = password

    @property
    def email(self) -> str:
        logger.debug('get email')
        return self._email
    
    @email.setter
    def email(self, value: str) -> None:
        logger.debug('set email to', value)
        self._email = value

    @property
    def password(self) -> str:
        logger.info('get password')
        return self._password
    
    @password.setter
    def password(self, value) -> None:
        logger.debug('set password to', value)
        self._password = value

user = User('email', 'password')
user.email
user.email = 'new_email'
