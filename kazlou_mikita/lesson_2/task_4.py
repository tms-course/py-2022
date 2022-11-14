a = input('Введите произвольную строку :  ')

even = (a[1::2])
odd = (a[::2])

print('Введена строка :', a, sep='', end=' '*2) 
print(even, odd, sep=' '*5, end='\n!!!')



