"""
Задание 1.

Написать лямбда-функцию определяющую чётное/нечётное.
Функция принимает параметр (число) и если чётное, 
то выдает слово "чётное", если нет — то "нечётное".
"""
even_or_odd = lambda num: "чётное" if num % 2 == 0 else "нечётное"
print(f"Even number: {even_or_odd(10)}")
print(f"Odd number: {even_or_odd(5)}")