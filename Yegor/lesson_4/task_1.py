def swap_dictionary(dictionary: dict) -> dict:
    return {key: value for value, key in dictionary.items()}


my_dictionary = {'a': 1,
                 'b': 2,
                 'c': 3}
dictionary = swap_dictionary(my_dictionary)
print(dictionary)





