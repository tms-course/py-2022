list_of_numbers = [1, 2, 3, 2, 3, 2, 1, 1, 1, 5, 3, 2]


def counter_numbers(number: int) -> int:
    global list_of_numbers
    counter, i = 0, 0
    while i < len(list_of_numbers):
        if list_of_numbers[i] == number:
            list_of_numbers.remove(list_of_numbers[i])
            counter += 1
        else:
            i += 1
    return counter


set_of_numbers = set(list_of_numbers)
dict_of_count_numbers = {}.fromkeys(set_of_numbers, 0)
for element in set_of_numbers:
    dict_of_count_numbers[element] = counter_numbers(element)

print(dict_of_count_numbers)

for key, value in dict_of_count_numbers.items():
    print(f'Сколько раз употребляется число {key} в массиве данных: {value}.')