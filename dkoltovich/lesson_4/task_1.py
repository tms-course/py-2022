def exchange_vals_and_keys(dictionary: dict) -> dict:
    new_dict = {values: keys for keys, values in dictionary.items()}
    return new_dict


my_dict = {1: 'a',
           2: 'b',
           3: 'c',
           4: 'd'}

new_dict = exchange_vals_and_keys(my_dict)
print(new_dict)
