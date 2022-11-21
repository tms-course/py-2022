from random import randint

puzzle_area = randint(1, 20)
attempts = 0
while True:
    attempts += 1
    r = int(input("число от 1 до 20 "))
    if r < puzzle_area:
        print("Число меньше загаданного. Попробуйте еще раз")
    if r > puzzle_area:
        print("Число больше чем загаданное. Попробуйте еще раз")
    if r == puzzle_area:
        print("Вы угадали, это число -", puzzle_area, "- Количество использованных попыток:", attempts)
        break
