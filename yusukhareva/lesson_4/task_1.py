def dict_orig(**kwargs):
    return {v: k for k, v in kwargs.items()}

d_swap = dict_orig(a= "Anna", b = "Boris")
print(d_swap)