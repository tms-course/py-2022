dct = {'a':1, 'b':3, 'c':2}
def invert (dct):
    return {val: key for key, val in dict.items(dct)}
print (invert(dct))