"""
To filter only palindromes in the tuple of words
"""
tuple_of_words = ('John', 'mom', 'eye', 'huh', 'print')
only_palindromes = tuple(filter(lambda word: word == word[::-1], tuple_of_words))
print(only_palindromes)