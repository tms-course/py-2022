x = str(input('Введите два слова: '))
first_word, second_word = x.split(" ")

#1
print ('!{} ! {}!'.format(second_word , first_word))
#2
print ('!%s ! %s!'%(second_word , first_word))
#3
print (f"!{second_word} ! {first_word}!")