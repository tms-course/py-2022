a = input()
even = a[::2]
uneven = a[1::2]
print('Введена строка:', a.strip(), end=2 * '\n')
print(even, uneven, sep='\t' * 5, end='\n!!!')
