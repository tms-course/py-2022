from string import punctuation
from collections import defaultdict
import argparse


parser = argparse.ArgumentParser(description='Words ranker')
parser.add_argument('-n', type=int, default=2, help='Provide an integer (default: 2)')
parser.add_argument('-k', type=int, default=2, help='Provide an integer (default: 2)')
arguments = parser.parse_args()

s = '''Что тебе, что мне, что ей, - всем нужно решить эту задачу,
    а что потом будет, потом и увидим, а увидим мы непременно'''


def get_list_of_words(text: str) -> list:
    text = text.lower()
    for i in range(len(text)):
        if text[i] in punctuation:
            text = text.replace(text[i], ' ')
    list_of_words = text.split()
    return list_of_words


def get_dict_counter_words(list_of_words: list) -> dict:
    dict_tmp ={}
    for element in list_of_words:
        if element in dict_tmp:
            dict_tmp[element] += 1
        else:
            dict_tmp[element] = 1
    return dict_tmp


def swap_dictionary(dict_tmp: dict) -> dict:
    dict_of_count_with_words = defaultdict(list)
    for key, value in dict_tmp.items():
        dict_of_count_with_words[value].append(key)
    dict_of_count_with_words = sorted(dict_of_count_with_words.items(), reverse=True)
    return dict(dict_of_count_with_words)


def printing_output(dict_of_count: dict):
    n_tmp = 0
    for key, value in dict_of_count.items():
        if n_tmp < arguments.n:
            str_tmp = ', '.join(dict_of_count[key][:arguments.k:])
            print(key, str_tmp)
            n_tmp += 1


def main():
    dict_of_count_with_words = swap_dictionary(get_dict_counter_words(get_list_of_words(s)))
    printing_output(dict_of_count_with_words)


main()