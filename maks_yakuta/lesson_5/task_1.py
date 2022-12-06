number = int(input('Введите любое число: '))
result = (lambda x: "четное" if x % 2 == 0 else "нечётное")(number)
print(result)