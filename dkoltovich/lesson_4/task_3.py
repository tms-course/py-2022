# дан список, посчитаь сколько раз втсречается каждое число метод гет или опертор ин
def counter(lst: list) -> dict:
    counter_dict = {i: 0 for i in lst}
    for number in lst:
        counter_dict[number] = counter_dict.get(number) + 1

    return counter_dict


lst = [1, 2, 3, 1, 2, 1, 2, 4, 5, 5, 5, 5]

print(counter(lst))
