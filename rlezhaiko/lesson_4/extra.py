from string import punctuation
import argparse


parser = argparse.ArgumentParser(description='Words ranker')
parser.add_argument('-n', type=int, default=2, help='Provide an integer (default: 2)')
parser.add_argument('-k', type=int, default=2, help='Provide an integer (default: 2)')
arguments = parser.parse_args()

s = '''Что тебе, что мне, что ей, - всем нужно решить эту задачу,
    а что потом будет, потом и увидим, а увидим мы непременно'''


def counter_words(word: str) -> int:
    global list_of_words
    counter, i = 0, 0
    while i < len(list_of_words):
        if list_of_words[i] == word:
            list_of_words.remove(list_of_words[i])
            counter += 1
        else:
            i += 1
    return counter


def transformation_text(text: str) -> dict:
    text = text.lower()
    for i in range(len(text)):
        if text[i] in punctuation:
            text = text.replace(text[i], ' ')

    global list_of_words
    list_of_words = text.split()
    set_of_words = set(list_of_words)
    dict_of_count_words_tmp = {}.fromkeys(set_of_words, 0)
    for element in set_of_words:
        dict_of_count_words_tmp[element] = counter_words(element)

    set_sorted_values = sorted(set(dict_of_count_words_tmp.values()), reverse=True)
    dict_of_count_words = {}.fromkeys(set_sorted_values, [])

    for element in set_sorted_values:
        list_of_word_with_counter = []
        for item in dict_of_count_words_tmp.items():
            if item[1] == element:
                list_of_word_with_counter.append(item[0])
        dict_of_count_words[element] = list_of_word_with_counter
    
    return dict_of_count_words


dict_of_count_words = transformation_text(s)
n_tmp = 0
for key, value in dict_of_count_words.items():
    if n_tmp < arguments.n:
        print(f'{key} {value[:arguments.k:]}')
        n_tmp += 1