def count_numbers(random_number: list) -> dict:
    dictionary = {}
    for y in random_number:
        dictionary[y] = dictionary.get(y, 0) + 1

    return dictionary


print(count_numbers(random_number))
