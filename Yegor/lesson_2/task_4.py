# 4th task
n = input("Введите произвольную строку: ")
odd = n[0:len(n):2]
even = n[1:len(n):2]
print('Введена строка:', n.strip(), end='  ')
print(odd, even, sep='     ', end='\n!!!!!')
