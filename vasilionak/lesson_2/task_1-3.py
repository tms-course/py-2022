a = b = c = 5
print(id(a), id(b), id(c))

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
print(id(list_1), id(list_2))

a = str("5")
b = float(5)
print(id(a), id(b), id(c))

list_1 = list_2
print(id(list_1), id(list_2))
