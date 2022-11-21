my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
my_new_dict = {v:k for k, v in my_dict.items()}  
print(my_new_dict)