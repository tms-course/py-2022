import string


# Task 1
even_numbers = list(range(0, 11, 2))
second_list_of_even_numbers = even_numbers
third_list_of_even_numbers = even_numbers
print("Task1: even_numbers, second_list_of_even_numbers and third_list_of_even_numbers " 
     f"share the same reference : {even_numbers is second_list_of_even_numbers is third_list_of_even_numbers}")


# Task 2
odd_numbers = list(range(1, 10, 2))
another_list_with_odd_numbers = odd_numbers.copy() 
print(f"Task2: odd_numbers list equals to another_lsit_with_odd_numbers: {another_list_with_odd_numbers == odd_numbers}. "
      f"However, they don't have shared reference: {odd_numbers is not another_list_with_odd_numbers}")


# Task 3
second_list_of_even_numbers = even_numbers.copy()
third_list_of_even_numbers = even_numbers.copy()
print("Task3: even_numbers, second_list_of_even_numbers and third_list_of_even_numbers "
     f"don't share the same reference : {even_numbers is not second_list_of_even_numbers is not third_list_of_even_numbers}")
another_list_with_odd_numbers = odd_numbers
print(f"Task3: another_list_with_odd_numbers and odd_numbers share the same reference: {another_list_with_odd_numbers is odd_numbers}")


# Task 4
user_input = input("Please enter any string: ").strip()
even_chars = user_input[::2]
odd_chars = user_input[1::2]
print(f"Введена строка \"{user_input}\"", end="".rjust(2))
print(even_chars, odd_chars, sep="".rjust(5), end="\n!!!\n")


# Extra task 
variable_name = input("Enter variable name: ")
valid_symbols = string.ascii_letters + string.digits + "_"
difference = set(variable_name) - set(valid_symbols)
is_valid_variable_name = bool(variable_name) and variable_name[0].isalpha() and not difference 
print(f"Is variable name {variable_name} valid? — {is_valid_variable_name}")
