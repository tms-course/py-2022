def flipped_dictionary (**kwargs):
    return {v: k for k, v in kwargs.items()}

new_dict = flipped_dictionary(a=5, b=7, c=9)

print(new_dict)
