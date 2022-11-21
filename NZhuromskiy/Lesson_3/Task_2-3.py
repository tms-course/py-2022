while True:
    name_input = input("Введите свое имя: ")
    age_input = int(input("Введите ваш возраст: "))

    if age_input <= 0:
        print("Ошибка, повторите ввод")
    elif 0 < age_input < 10:
        print(f"Привет, шкет {name_input}")
    elif 10 <= age_input <= 18:
        print(f"Как жизнь, {name_input}?")
    elif 18 < age_input < 100:
        print(f"Что желаете, {name_input}?")
    else:
        print(f"{name_input}, вы лжете - в наше время столько не живут...")
