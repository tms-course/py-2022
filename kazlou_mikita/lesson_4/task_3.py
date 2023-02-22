my_list = [1, 1, 1, 1, 2, 5, 5, 5, 6, 2, 6]

def element_counter(any_list: list) -> dict:
    my_dict = {}
    for i in any_list:
        my_dict[i] = my_dict.get(i, 0) + 1
        
    return my_dict

print(element_counter(my_list))        