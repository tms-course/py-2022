tuple_of_words = ('John', 'mom', 'eye', 'huh', 'print')
only_palindroms = tuple(filter(lambda word: word == word[::-1], tuple_of_words))
print(only_palindroms)