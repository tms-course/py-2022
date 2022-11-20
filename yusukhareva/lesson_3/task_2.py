name = str (input ('Enter your name: '))
age = input ('Enter your age: ')
try:
    age = int(age)
    if age > 0 and age <=10:
        print (f'Привет, шкет {name}')
    elif age >10 and age <= 18:
        print ( f'Как жизнь, {name}?')
    elif age >18 and age <=100:
        print (f'Что желаете, {name}?')
    elif age >100:
        print (f'{name}, Вы лжете, в наше время столько не живут...')
    elif age <=0:
        print ('Ошибка, повторите ввод')
except:
    print ('Ошибка, повторите ввод')