user_input = int(input('Enter the number: '))
print('Четное' if (lambda x: x % 2 == 0)(user_input) else 'Нечетное')