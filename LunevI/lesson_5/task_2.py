"""
Дан список чисел. Возвращается список, где при помощи функции map() каждое число
переведено в строку. В качестве функции в map используется lambda.
"""
my_list = [2, 3, 5, 6, 1, 2, 3]
my_string_list = map(lambda x: str(x), my_list)
print(list(my_string_list))
