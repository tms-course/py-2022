#solution №1
def count_numbers(random_number: list) -> dict:
    dictionary = {x: 0 for x in random_number}
    for y in random_number:
        dictionary[y] += 1

    return dictionary


random_number = [1, 1, 4, 3, 2, 2, 1, 3, 1, 2, 3, 1, 4, 1]
dictionary = count_numbers(random_number)
print(dictionary)


#solution №2
def count_numbers(random_number: list) -> dict:
    dictionary = {}
    for y in random_number:
        dictionary[y] = dictionary.get(y, 0) + 1

    return dictionary


print(count_numbers(random_number))
