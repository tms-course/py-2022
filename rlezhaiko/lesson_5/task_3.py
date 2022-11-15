def check_palindrome(string:str) -> bool:
    """
    Check palindrom function.
    
    :param word: the word to check for a palindrom
    :returns: return True if the word is a palindrom, False otherwise
    """
    string = string.lower()
    return string == string[::-1]


tuple_of_words = ('Radar', 'apple', 'Madam', 'Tree', 'some', 'level', 'nun')
tuple_of_palindroms = tuple(filter(check_palindrome, tuple_of_words))
print(tuple_of_palindroms)