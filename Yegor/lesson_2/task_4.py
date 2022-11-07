# 4th task
x = input("Введите произвольную строку: ")
odd = x[0:len(x):2]
even = x[1:len(x):2]
print('Введена строка:', x.strip(), end='  ')
print(odd, even, sep='     ', end='\n!!!!!')
