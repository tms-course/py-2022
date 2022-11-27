"""
Из кортежа слов отфильтровываем полиндромы, при помощи функции filter().
"""
my_tuple = ('dad', 'tuple', 'list', 'level', 'sos')
palindroms = tuple(filter(lambda x: x == x[::-1], my_tuple))
print(list(palindroms))
