"""
3. При помощи функции filter() из кортежа слов отфильтровать только те, которые являются палиндромами (которые читаются
одинаково в обе стороны).
"""

tuple_w = ('level', 'toot', 'town', 'nun', 'peep', 'forest')

palindromes = tuple(filter(lambda words: words == words[::-1], tuple_w))

print(palindromes)
