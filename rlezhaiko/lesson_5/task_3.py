"""
3. При помощи функции filter() из кортежа слов отфильтровать только те, которые
являются полиндромами (которые читаются одинаково в обе стороны)
"""

def check_palindrome(string: str) -> bool:
    """
    Check palindrom function.
    
    :param string: the string to check for a palindrom
    :returns: return True if the word is a palindrom, False otherwise
    """
    string = string.lower()
    return string == string[::-1]


tuple_of_words = ('Radar', 'apple', 'Madam', 'Tree', 'some', 'level', 'nun')
tuple_of_palindroms = tuple(filter(check_palindrome, tuple_of_words))
print(tuple_of_palindroms)