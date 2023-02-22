

def count_element(my_list: list):
    count_map = {}
    for element in my_list:
        count_map[element] = count_map.get(element, 0) + 1

    return count_map

list = [1, 8, 1, 4, 8, 1, 6, 6, 8, 1, 5, 9]
print(count_element(list))
