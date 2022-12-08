"""
Задание 4.

Сделать функцию валидации email адресов при помощи регулярных выражений. Общий
вид email адреса "username@hostname":
    (a) username может состоять из латиницы, цифр, таких символов как !#%&'*+-/=?^_`{~}|
    и точки, за исключением первого и последнего знака, которая не может повторяться.

    (b) hostname состоит из нескольких компонентов, разделенных точкой и не превышающих 
    63 символа. Компоненты, в свою очередь, состоят из латинских букв, цифр
    и дефисов, причем дефисы не могут быть в начале или в конце компонента
"""
import re


class ValidationException(Exception):
    pass


def is_valid_email(email: str) -> bool:
    """
    Validates if email correct, or not.

    Args:
        email (str): Email which need to be verified
    
    Returns:
        bool: True if email is valid, else False
    """
    USERNAME_PATTERN = r"^[^.]([.]?[\w!#%&'\/=?^_`{~}+*-]+)+\b"
    HOSTNAME_PATTERN = r"^[^-][\w-]+\.[\w-]{1,63}$\b"

    try:
        username, hostname = email.split("@")
        hostname_match = re.match(HOSTNAME_PATTERN, hostname)
        username_match = re.match(USERNAME_PATTERN, username)
        if username_match:
            username_match_valid = username_match.group() == username
            return True if hostname_match and username_match_valid else False
        return False
    except ValueError:
        raise ValidationException(f"Provided email {email} is not valid.")


print(is_valid_email("te..st.name@username.com")) # False. Double dot in the username
print(is_valid_email("te.st.name@username.com")) # True.
print(is_valid_email("testname@username.com")) # True.
print(is_valid_email("TestUserName@GmaIL.COM")) # True
print(is_valid_email(".testname@username.com")) # False. Dot in the beggining of the username.
print(is_valid_email("testname@-username.com")) # False. Dash in the beggining of the hostname
print(is_valid_email("testname@username.com-")) # False. Dash on the end of the hostname
print(is_valid_email("testname")) # Error will be raised