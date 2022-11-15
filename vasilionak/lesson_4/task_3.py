

def count_element(my_list: list):
    count = {}
    for element in my_list:
        if count.get(element, None):
            count[element] += 1
        else:
            count[element] = 1
    return count

list = [1, 8, 1, 4, 8, 1, 6, 6, 8, 1, 5, 9]
print(count_element(list))


