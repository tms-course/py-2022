import re


def is_email_valid(email: str) -> bool:
    """
    Function that checks if email is valid
    :param email: email to check
    :return: True if email is valid, False otherwise
    """
    valid_username_exp = r'^[\d\w!#%&\'\*\+\-=\/\?\^\_\{\}\|\~]+[.]?[\d\w!#%&\'\*\+\-=\/\?\^\_\{\}\|\~]+'
    valid_hostname_exp = r'[^\-]([\w\d\-]{1,63}\.?)+[^\-\.]$'
    return re.fullmatch(valid_username_exp + r'@' + valid_hostname_exp, email) is not None


print(is_email_valid("11!3#koltovich@yand-ex.me.ru"))    # True
print(is_email_valid("11!3#ko.lto.vich@yand-ex.me.ru"))  # False
print(is_email_valid("11!3#koltov.ich@yand-ex.me.ru"))   # True
print(is_email_valid("11!3#koltovich@-yand-ex.me.ru-"))  # False
