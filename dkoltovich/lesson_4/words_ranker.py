import sys
from collections import defaultdict

input_text = '''Что тебе, что мне, что ей - всем нужно решить эту задачу,
а что потом будет, потом и увидим, а увидим мы непременно.'''


def get_arguments():
    [n, k] = [sys.argv[2], sys.argv[4]] if sys.argv[1] == '-n' else [sys.argv[4], sys.argv[2]]
    return int(n), int(k)


def swap_keys_with_values(dictionary: dict) -> dict:
    swap_dict = defaultdict(list)
    for key, value in dictionary.items():
        swap_dict[value].append(key)
    return swap_dict


def count_elements(list_of_items: list) -> dict:
    amount_of_elements = {}
    for item in list_of_items:
        amount_of_elements[item] = amount_of_elements.get(item, 0) + 1

    '''возращает словарь, где ключи - слова, а значения - кол-во раз, которое они встретились в тексте'''
    return amount_of_elements


def create_list_of_words(text: str) -> list:
    text = text.replace('.', '').replace(',', '')
    return [word.lower() for word in text.split() if word.isalpha()]


def create_counter_dict(list_of_words: list) -> dict:
    counter_dict = count_elements(list_of_words)  # словарь, где ключи - слова, а значения - сколько раз она встретились
    counter_dict = swap_keys_with_values(counter_dict)
    '''возращает отсортированный по убыванию словарь, где значения - слова, 
       а ключи - сколько раз они встретились в тексте'''
    return dict(sorted(counter_dict.items(), reverse=True))


amount_dictionary = create_counter_dict(create_list_of_words(input_text))
n_argument, k_argument = get_arguments()
for key in amount_dictionary.keys():
    if n_argument == 0:
        break
    print(key, ', '.join(amount_dictionary[key][:k_argument:]))
    n_argument -= 1
