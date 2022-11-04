# Задание 1
x1 = '10'
x2, x3 = x1, x1
print(id(x1), id(x2), id(x3))

# Задание 2
y1 =[1, 2, 3]
y2 = [1, 2, 3]
print(id(y1), id(y2))

# Задание 3
x1, x2, x3 = list(x1), set(x2), list(x3)
print(id(x1), id(x2), id(x3))
y1 = tuple(y1)
y2 = y1
print(id(y1), id(y2))
