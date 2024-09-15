# task_1
dct = {'key': 'val'}
res = {v: k for k, v in dct.items()}

print(dct)
print(res)
# task_2
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
print(fac(5))
# task_3
