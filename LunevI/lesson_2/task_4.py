# task 4

text = input('введите произвольную строку: ')
chet = text[1::2]
ne_chet = text[0::2]
print('введена строка', text.strip(), sep=' "', end='"\n  ')

print(chet, ne_chet, sep=' '*5, end='\n!!!')
