full_str = input('Введите строку: ')

full_str = full_str.strip()
even_symbols = full_str[1::2]
odd_symbols = full_str[0::2]

print('Введена строка: "', full_str, '"', sep='', end='\n\n')
print(even_symbols, odd_symbols, sep='     ', end='\n!!!')