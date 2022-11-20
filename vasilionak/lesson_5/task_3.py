words = ('wow', 'world', 'mom', 'cat', 'eye')
filtered_list = (list(filter(lambda item: item == item[::-1], words)))
print(filtered_list)
"""
отфильтровывает слова и выдает только те что являются полиндромами
"""