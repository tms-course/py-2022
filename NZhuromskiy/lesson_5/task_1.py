"""
1. Написать лямбда-функцию определяющую чётное/нечётное. Функция принимает параметр (число) и если чётное,
то выдаёт слово "чётное", если нет - то "нечётное".
"""

user_count = int(input("Введите число: "))

print((lambda count: "чётное" if count % 2 == 0 else "нечётное")(user_count))
