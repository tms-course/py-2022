x = int(input("Введите число: "))
answer = (lambda x: "четное" if x % 2 == 0 else "нечетное")(x)
"""
принимает число и выдает четное оно или нет
param x: number for check 
param answer: return result
"""
print(answer)