""" 
4. Сделать функцию валидации email адресов при помощи регулярных выражений. Общий
вид email адреса "username@hostname"
(a) username может состоять из латиницы, цифр, таких символов как !#%&'+-/=?^_`{~}|
и точки, за исключением первого и последнего знака, которая не может повторяться
(b) hostname состоит из нескольких компонентов, разделенных точкой и не превышающих
63 символа. Компоненты, в свою очередь, состоят из латинских букв, цифр 
и дефисов, причем дефисы не могут быть в начале или в конце компонента.
"""
import re


def email_validation(email: str) -> bool:
    """ 
    Checks email for the following conditions:
    (a) username may consist of latin characters, numbers, characters such 
    as !#%&'+-/=?^_`{~}| and a dot, except for the first and last character, which cannot be repeated.
    (b) hostname consists of multiple components, separated by a dot, and not exceeding 63 characters. 
    Components, in turn, consist of Latin letters, numbers and hyphens, and hyphens cannot be at the 
    beginning or at the end of the component.
    
    :param email: email which need check for valid
    :returns: return True if email valid, False otherwise
    """
    try:
        username, hostname = email.split('@')
        
        user_regular_pattern = r"^[^.]([\.]?[\w!#%&'\+\-/=\?\^_`\{~\}\|])+[^.]$"
        if not re.match(user_regular_pattern, username):
            return False
        
        host_regular_pattern = r'^[^-][\w\.-]{1,61}[^-]$\b'
        if not re.match(host_regular_pattern, hostname):
            return False
    except ValueError:
        return False
   
    return True


# Username tests
print(email_validation('example@gmail@com'))      # False. More then one @ in email
print(email_validation('example@gmail.com'))      # True
print(email_validation('exam.ple@gmail.com'))     # True
print(email_validation('.example@gmail.com'))     # False. Dot at the beggining of username
print(email_validation('example.@gmail.com'))     # False. Dot at the end of username
print(email_validation('exam..ple@gmail.com'))    # False. Two dots in a row

# Hostname tests
print(email_validation('example@gmail.com'))                                                           # True
print(email_validation('example@gmailllllllllllllllllllllllllllllllllllllllllllllllllllllll.com'))     # True
print(email_validation('example@gmail.com-'))                                                          # False. hyphens at the end of hostname
print(email_validation('example@-gmail.com'))                                                          # False. hyphens at the beggining of hostname
print(email_validation('example@gm-ail.com'))                                                          # True