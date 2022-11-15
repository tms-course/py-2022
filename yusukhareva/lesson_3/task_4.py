i = 0
n = int (input ('Введите число: '))
x = 0
while i <= n :    
    x+=i**3
    i+=1
     
print (x)
x+=i**3



i = 0
n = int (input ('Введите число: '))
x = 0
for i in range (n) :    
    x+=i**3
    i+=1


x+=i**3
print (x)