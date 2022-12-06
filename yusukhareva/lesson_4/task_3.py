from collections import Counter
num_lst = [1,2,3,4,5,6,8,2,5,4,6,6,5,6,3,6,0,7,3]
#первый способ
count_num = Counter(num_lst)
print (count_num)

#второй способ (по доп.условию)
dict_num = {}
for num in num_lst:
    if dict_num.get(num):
        dict_num[num] += 1
    else:
        dict_num[num] = 1

print(dict_num)

     


    