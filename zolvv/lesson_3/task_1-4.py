# first quest
a = 1
b = 1
c = 1
print(id(a),id(b),id(c),id(a) == id(b),id(b) == id(c),id(a) == id(c))
# second quest
d = ['3']
e = ['3']
print(id(d),id(e))
# third quest
a = str(a)
b = str(b)
c = str(c)
d = bool(d)
e = bool(c)
print(id(a),id(b),id(c),id(d),id(e))
# fourth quest
x = input("Введите произвольную строку: ")
first = x[0:len(x):2]
second = x[1:len(x):2]
print('Введена строка "', x.strip(), '"', sep='', end=' ' * 2)
print(first, second, sep=' ' * 5, end='\n!!!')
print(f"Введена строка \"{x.strip()}\"", end="".rjust(2))
print(first, second, sep="".rjust(5), end="\n!!!")
