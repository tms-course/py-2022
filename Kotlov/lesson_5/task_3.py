
tuple_word = ('that', 'from', 'deed', 'product', 'peep', 'level', 'add')

print(*list(filter(lambda x: x == x[::-1], tuple_word)))
