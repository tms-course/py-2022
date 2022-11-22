# task 1
a = 7
b = 7
c = 7
print (id (a), id (b), id (c))

# task 2
a = [7, 8, 9]
b = [7, 8, 9]
print (id (a), id (b))

# task 3
a = 7
b = 7
c = 7
print (id (a), id (b), id (c))
a = str (a)
b = str (b)
c = str (c)
print (id (a), id (b), id (c))

a = [7, 8, 9]
b = [7, 8, 9]
print (id (a), id (b))
a = bool (a)
b = bool (b)
print (type (a), type (b))

# task 4
line = input ('Введите произвольную строку')
odd_symbols = line [0::2]
even_symbols = line [1::2]

print ('Введена строка :', line)
print ('Введена строка :', line, ' '*2, odd_symbols, ' '*5, even_symbols, '\n!!!')



