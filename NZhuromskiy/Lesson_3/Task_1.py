#Вариант 1
entering_words = input("Введите два слова: ").split(' ')
format_operator = "!%s ! %s!" % (entering_words[1], entering_words[0])
print(format_operator)

#Вариант 2
entering_words = input("Введите два слова: ").split(' ')
format_s = "!{0} ! {1}!".format(entering_words[1], entering_words[0])
print(format_s)



#Вариант 3
entering_words = input("Введите два слова: ").split(' ')
format_f = f"!{entering_words[1]} ! {entering_words[0]}!"
print(format_f)