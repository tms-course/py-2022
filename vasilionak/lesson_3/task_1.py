words = input("Введите предложение из двух слов: ").split(" ")
s = "!{0} ! {1}!".format(words[1], words[0])
print(s)

k = f"!{words[1]} ! {words[0]}!"
print(k)

j = '!%s ! %s!' % (words[1], words[0])
print(j)
