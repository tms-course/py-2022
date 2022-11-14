list_of_numbers = [i for i in range(20)]
list_of_numbers_in_str_format = list(map(lambda x: str(x), list_of_numbers))
print(list_of_numbers_in_str_format)