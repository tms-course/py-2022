def my_func(**kwargs):
    keys, values = [], []
    for key, value in kwargs.items():
        print(value, key)
        keys.append(key)
        values.append(value)
    return values, keys
keys, values = my_func(a=5, b=7, c=9)