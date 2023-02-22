# task 1
# string
words = input ('Введите предложение из двух слов'). split (' ')
change_words = '! {0} ! {1}!'.format(words [1], words [0])
print (change_words)

#f-string
words = input ('Введите предложение из двух слов'). split (' ')
change_words = f'! {words[1]} ! {words[0]}!'
print (change_words)

#%s
words = input ('Введите предложение из двух слов'). split (' ')
change_words = '!%s ! %s!' % (words[1], words[0])
print (change_words)

# task 2

name = input('Введите своё имя')
age = int(input ('Сообщите свой возраст'))
if age <= 0:
    print ('Ошибка, повторите ввод')
elif age > 0 and age < 10:
    print ("Привет Шкет", name, sep = ',')
elif age >= 10 and age <18:
    print ("Как жизнь", name, sep = ',')
elif age >= 18 and age <100:
    print ("Что желаете?", name, sep = ',')
else:
    print (name, "вы лжёте", sep = ',')

#task 3
while True:
    name = input('Введите своё имя')
    age = int(input ('Сообщите свой возраст'))
    if age <= 0:
        print ('Ошибка, повторите ввод')
    elif age > 0 and age < 10:
        print ("Привет Шкет", name, sep = ',')
    elif age >= 10 and age <18:
        print ("Как жизнь", name, sep = ',')
    elif age >= 18 and age <100:
        print ("Что желаете?", name, sep = ',')
    else:
        print (name, "вы лжёте", sep = ',')

#task 4
number = int(input("Введите целое число: "))
result = 0
for i in range(1, number + 1):
    result = result + i ** 3
print(result)

number = int(input('Введите целое число: '))
i = 1
result = 0
while i <= number:
    result = result + i**3
    i = i + 1
print(result)


