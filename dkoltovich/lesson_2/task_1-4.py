# 1st task
a = 3
b = 3
c = 3
print('first task:\n', id(a) == id(b) and id(b) == id(c) and id(a) == id(c))

# 2nd task
string1 = [1]
string2 = [1]
print("second task:\n", id(string1) != id(string2))

# 3rd task
a = str(a)
b = str(b)
c = str(c)
string1 = bool(string1)
string2 = bool(string2)
print('third task:\n', id(a) != id(b) and id(b) != id(c) and id(a) != id(c) and id(string1) == id(string2))

# 4th task
x = input("Введите произвольную строку: ")
first = x[0:len(x):2]
second = x[1:len(x):2]

print('Введена строка "', x.strip(), '"', sep='', end=' ' * 2)
print(first, second, sep=' ' * 5, end='\n!!!')
# или вместо пробелов
# rjust делает выравнивание
print(f"Введена строка \"{x.strip()}\"", end="".rjust(2))
print(first, second, sep="".rjust(5), end="\n!!!")
