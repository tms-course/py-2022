sentence = input('Введите предложение из двух слов : ').split(' ')
x = '!{1} ! {0}!'.format(sentence[0], sentence[1])
y = f'!{sentence[1]} ! {sentence[0]}!'
z = '!%s ! %s!' % (sentence[1], sentence[0])
print(x, y, z, sep='\n')

