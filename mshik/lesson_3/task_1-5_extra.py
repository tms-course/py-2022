import sys
from random import randint


# Task 1
sentense = input("Please enter any sentense: ")
reversed_sentense = " ! ".join(sentense.split()[::-1])
print("!{sentense}!".format(sentense=reversed_sentense))
print(f"!{reversed_sentense}!")
print("!%s!" % reversed_sentense)


# Task 4
# With for loop
n = int(input("Введите целое число: "))
sum_of_cubes = 0
for int_num in range(1, n + 1):
    sum_of_cubes += int_num ** 3
print(f"Сумма кубов: {sum_of_cubes}")

# With while loop
sum_of_cubes = 0
while n:
    sum_of_cubes += n ** 3
    n -= 1
print(f"Сумма кубов: {sum_of_cubes}")
    

# Task 5
random_int = randint(0, 100)
while True:
    guess_number = input("Введите число в диапозоне от 0 до 100: ")
    if not guess_number.isdigit():
        print(f"{guess_number} не число")
        continue

    guess_number = int(guess_number) 
    if random_int > guess_number:
        print("Число меньше чем загаданное")
    elif random_int < guess_number:
        print("Число больше чем загаданное")
    else:
        print("Вы угадали")
        break


# Extra task
print("\nДополнительная задача, вводите операции ниже этой строки:")
stack = []
for line in sys.stdin:
    if not line.strip():
        continue

    operation, *operands = line.split()
    values = "".join(operands).split(",")
    if operation == "add":
        stack.extend(values)
    elif operation == "view":
        print(stack)
        continue
    elif operation == "rm":
        for value in values:
            if value not in stack:
                print(f"Элемента {value} нет в коллекции.")
            else:
                stack.remove(value)
    elif operation == "quit":
        break
    else:
        print("Я не поддерживаю такую операцию")


# Task 2 & 3
while True:
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод.")
    age = int(age)
    
    if 0 < age < 10:
        print(f"Как жизнь {name}?")
    elif 10 <= age <= 18:
        print(f"Привет, шкет {name}")
    elif 18 < age < 100:
        print(f"Что желаете {name}?")
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")