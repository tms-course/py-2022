def swap_keys_with_values(dictionary: dict) -> dict:
    return {values: keys for keys, values in dictionary.items()}


my_dict = {1: 'a',
           2: 'b',
           3: 'c',
           4: 'd'}

new_dict = swap_keys_with_values(my_dict)
print(new_dict)
