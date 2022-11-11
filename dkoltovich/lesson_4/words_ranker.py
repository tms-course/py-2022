import sys


def parse_arguments(line_of_arguments: str):
    n_index = line_of_arguments.find('-n')
    k_index = line_of_arguments.find('-k')
    if n_index > k_index:
        n_index, k_index = k_index, n_index
        k, n = line_of_arguments[n_index + 2: k_index], line_of_arguments[k_index + 2::]
    else:
        n, k = line_of_arguments[n_index + 2: k_index], line_of_arguments[k_index + 2::]

    return int(n), int(k)


def swap_keys_with_values(dictionary: dict) -> dict:
    swap_dict = {}
    for key, value in dictionary.items():
        swap_dict[value] = swap_dict.get(value, []) + [key]
    return swap_dict


def counter(list_of_items: list) -> dict:
    amount_of_elements = {i: 0 for i in list_of_items}
    for item in list_of_items:
        amount_of_elements[item] = amount_of_elements.get(item) + 1

    return amount_of_elements


def count_words_amount(text: str) -> dict:
    text = text.replace('.', '').replace(',', '')
    list_of_words = [word.lower() for word in text.split() if word.isalpha()]
    dictionary = counter(list_of_words)  # словарь, где ключи - слова, а значения - сколько раз она встретились
    dictionary = swap_keys_with_values(dictionary)
    '''возращает отсортированный по убыванию словарь, где значения - слова, 
       а ключи - сколько раз они встретились в тексте'''
    return dict(sorted(dictionary.items(), reverse=True))


input_txt = '''Что тебе, что мне, что ей - всем нужно решить эту задачу,
а что потом будет, потом и увидим, а увидим мы непременно.'''
amount_dictionary = count_words_amount(input_txt)
arguments_line = ''.join(sys.argv)
n_argument, k_argument = parse_arguments(arguments_line)
for i in range(n_argument):
    print(''.join([str(key) for key in amount_dictionary.keys()]))