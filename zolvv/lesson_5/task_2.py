"""
To convert each element in list into string with the help of map(lambda, [])
"""
list_of_numbers = [1, 2, 5, 6, 7, 8, 9, 10]
list_of_string_num = list(map(lambda x: str(x), list_of_numbers))
print(list_of_string_num)