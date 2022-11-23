from sys import argv

if argv[1] == '-n':
    n = int(argv[2])
    k = int(argv[4])
else:
    k = int(argv[2])
    n = int(argv[4])

our_text = input().lower()  # Вводим наш текст и приводим его к одинаковому регистру

for i in our_text:  # Удаляем все не нужные элементы
    if not i.isalpha():
        our_text = our_text.replace(i, ' ')

our_text = our_text.split()  # Делаем список из элементов(слов) строки our_text

word_count = {}  # Создаём словарь элементами которого являются слова и их количество в тексте
for i in our_text:
    word_count[i] = word_count.get(i, 0) + 1

word_count_2 = {}

for key, value in word_count.items():
    if value in word_count_2:
        word_count_2[value] = word_count_2.get(value) + [key]
    else:
        word_count_2[value] = [key]

count_n = 0

while count_n < n:
    max_key = max(word_count_2)
    print(max_key, end=' ')
    print(*word_count_2[max_key][:k], sep=', ')
    count_n += 1
    del word_count_2[max_key]
    if word_count_2 == {}:
        break
