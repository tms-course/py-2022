list_numbers = [2,3,4,2,3,5,6,7,8,5,4,3,3,4,5,6,7,8,9]
def amount_element(list: list):
    my_dict = {}
    for element in list:
        my_dict[element] = my_dict.get(element, 0) + 1

    return my_dict


print(amount_element(list_numbers))