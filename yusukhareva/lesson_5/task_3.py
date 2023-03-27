""" Filters palindromes from tuple
:param words: tuple of different words
"""
print (tuple(filter(lambda words: words==words[::-1], ('eve', 'adam', 'pit', 'elemele', 'cat','Ana'))))
