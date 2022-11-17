def swap_dictionary(dictionary: dict) -> dict:
    return {keys: values for values, keys in dictionary.items()}


my_dictionary = {'a': 1,
                 'b': 2,
                 'c': 3}
print(my_dictionary.items())
dictionary = swap_dictionary(my_dictionary)
print(dictionary)





