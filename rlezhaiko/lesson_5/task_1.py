"""
1. Написать лямбда-функцию определяющую четное/нечетное. Функция принимает
параметр (число) и если четное, то выдает слово "четное", если нет - то "нечетное".
"""

user_input = int(input('Enter the number: '))
print((lambda x: 'Четное' if x % 2 == 0 else 'Нечетное')(user_input))
