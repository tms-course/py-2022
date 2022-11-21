list_2_words = input('Введите предложение из 2 слов: ').split()

print('{1} {0}'.format(list_2_words[0], list_2_words[1]))
print(f'!{" ".join(list_2_words[::-1])}!')
print('%s ! %s' % (list_2_words[0], list_2_words[1]))
