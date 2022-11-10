list_of_numbers = [1, 2, 3, 2, 3, 2, 1, 1, 1, 5, 3, 2]

def counter_numbers(number: int, list_of_numbers: list) -> int:
    counter = 0
    for element in list_of_numbers:
        if element == number:
            counter += 1
    return counter


set_of_numbers = set(list_of_numbers)
dict_of_count_numbers = {}.fromkeys(set_of_numbers, 0)
for element in set_of_numbers:
    dict_of_count_numbers[element] = counter_numbers(element, list_of_numbers)

print(dict_of_count_numbers)