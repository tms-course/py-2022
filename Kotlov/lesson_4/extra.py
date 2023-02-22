from sys import argv

n = argv[argv.index('-n') + 1]
k = argv[argv.index('-k') + 1]  # так argv хранит все в списке мы можем достать любой элемент

our_text = input().lower()  # Вводим наш текст и приводим его к одинаковому регистру

for i in our_text:  # Удаляем все не нужные элементы
    if not i.isalpha():
        our_text = our_text.replace(i, ' ')

our_text = our_text.split()  # Делаем список из элементов(слов) строки our_text

word_count = {}  # Создаём словарь элементами которого являются слова и их количество в тексте
for i in our_text:
    word_count[i] = word_count.get(i, 0) + 1

number_of_different_words = {}

for key, value in word_count.items():
    if value in number_of_different_words:
        number_of_different_words[value] = number_of_different_words.get(value) + [key]
    else:
        number_of_different_words[value] = [key]

count_n = 0

while count_n < n:
    max_key = max(number_of_different_words)
    print(max_key, end=' ')
    print(*number_of_different_words[max_key][:k], sep=', ')
    count_n += 1
    del number_of_different_words[max_key]
    if number_of_different_words == {}:
        break
