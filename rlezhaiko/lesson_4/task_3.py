list_of_numbers = [1, 2, 3, 2, 3, 2, 1, 1, 1, 5, 3, 2]


def get_dict_counter_numbers(list_of_numbers: list) -> dict:
    dict_tmp ={}
    for element in list_of_numbers:
        if element in dict_tmp:
            dict_tmp[element] += 1
        else:
            dict_tmp[element] = 1
    return dict_tmp
    

dict_of_count_numbers = get_dict_counter_numbers(list_of_numbers)
print(dict_of_count_numbers)
for key, value in dict_of_count_numbers.items():
    print(f'Сколько раз употребляется число {key} в массиве данных: {value}.')