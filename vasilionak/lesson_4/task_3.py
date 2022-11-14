
def count_element(list):
    count = {}
    for element in list:
        if count.get(element, None):
            count[element] += 1
        else:
            count[element] = 1
    return count

print(count_element(list))


