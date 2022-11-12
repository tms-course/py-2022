list_of_numbers = [1, 2, 3, 2, 3, 2, 1, 1, 1, 5, 3, 2]

def counter_numbers(number: int) -> int:
    # counter = 0
    # for element in list_of_numbers:
    #     if element == number:
    #         counter += 1
    # return counter
    global list_of_numbers
    counter, i = 0, 0
    while i < len(list_of_numbers):
        print(list_of_numbers)
        #print(len(list_of_numbers))
        if list_of_numbers[i] == number:
            #print(list_of_numbers[i])
            list_of_numbers.remove(list_of_numbers[i])
            counter += 1
            #i -= 1
        else:
            i += 1
    return counter


set_of_numbers = set(list_of_numbers)
dict_of_count_numbers = {}.fromkeys(set_of_numbers, 0)
for element in set_of_numbers:
    dict_of_count_numbers[element] = counter_numbers(element)

print(dict_of_count_numbers)