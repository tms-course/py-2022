import keyword

a = input('Как вы хотите назвать переменную?\n')
b = list(a)
c = a.replace('_', 'a')
bool_value = not (' ' in b or b[0].isdigit() or keyword.iskeyword(a) or not c.isalnum())

print(f'Is variable name "{a}" valid ? - {bool_value}')

