import re

r'[a-zA-Z0-9]+'
r'[hello]'

username_re = r'^[^.](\.?[A-Za-z0-9!#%&\'*+-/=?^_`{~}]+)+'


def validate_email(email_address: str) -> bool:
    