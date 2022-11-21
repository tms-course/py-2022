#Вариант 1
enter_a_number = int(input("Необходимо ввести любое целое число: "))
result = 0
for i in range(1, enter_a_number + 1):
    result = result + i ** 3
print(result)


#Вариант 2
enter_a_number = int(input("Необходимо ввести любое целое число: "))
i = 1
result = 0
while i <= enter_a_number:
    result = result + i**3
    i = i + 1
print(result)