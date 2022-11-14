def check_palindrome(string:str) -> bool:
    string = string.lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False


tuple_of_words = ('Radar', 'apple', 'Madam', 'Tree', 'some', 'level', 'nun')
tuple_of_palindroms = tuple(filter(check_palindrome, tuple_of_words))
print(tuple_of_palindroms)