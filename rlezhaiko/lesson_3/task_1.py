# 1-ый способ (string.format())
words = input('Введите предложение из двух слов: ').split(' ')
s = '!{0} ! {1}!'.format(words[1], words[0])
print(s)

# 2-ой способ (f-string)
words = input('Введите предложение из двух слов: ').split(' ')
s = f'!{words[1]} ! {words[0]}!'
print(s)

# 3-ий способ (%s)
words = input('Введите предложение из двух слов: ').split(' ')
s = '!%s ! %s!' % (words[1], words[0])
print(s)