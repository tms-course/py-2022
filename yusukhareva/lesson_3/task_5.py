x = 11

while True:
    y = int (input ('Угадайте число: '))
    if abs(x - y) > 10:
        print ('Холодно')
    elif abs(x - y)<=10 and abs(x - y)>5:
        print ('Теплее')
    elif abs(x - y)<=5 and  abs(x - y)>=1:
        print('Горячо')
    elif y == x:
        print('УРА! Вы угадали!') 
        break
    
