variable_name = input('Введите название переменной: ').replace('_', 'a')

flag_1 = variable_name[0].isalpha()
flag_2 = variable_name[1:].isalnum()
is_valid = bool(flag_1 * flag_2)

print('Is variable name', variable_name, 'valid?', is_valid)

