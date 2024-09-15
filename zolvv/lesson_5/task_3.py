"""
Filter only palindromes in the tuple of words
"""
tuple_of_words = ('deed', 'dad', 'eye', 'level', 'hello', 'boy')
only_palindromes = tuple(filter(lambda word: word == word[::-1], tuple_of_words))
print(only_palindromes)