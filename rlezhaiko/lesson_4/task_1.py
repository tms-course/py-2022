my_dict_1 = {1: 'a',
             2: 'b',
             3: 'c',
             4: 'd'}

my_dict_2 = {value:key for key, value in my_dict_1.items()}
print(my_dict_1, my_dict_2, sep='\n')