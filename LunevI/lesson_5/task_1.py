"""
Лямбда функция, определяющая четное/нечетное. Принимает
параметр (число) и если четное, то выдает слово "четное", если нет - то "нечетное".
"""
number = int(input('Введите число: '))
result = (lambda x: "четное" if x % 2 == 0 else "нечентное")(number)
print(result)