while True:
    name = input("Введите имя:")
    age = int(input("Введите Ваш возраст: "))
    if age <= 0:
        print("Ошибка, повторите ввод")
    elif 0 < age < 10:
        print(f"Привет, шкет {name}")
    elif 18 >= age >= 10:
        print(f"Как жизнь, {name}?")
    elif 18 < age < 100:
        print(f"Что желаете, {name}?")
    else:
        print(f"{name} вы лжете - в наше время столько не живут...")
