from string import punctuation


s = '''Что тебе, что мне, что ей, - всем нужно решить эту задачу,
    а что потом будет, потом и увидим, а увидим мы непременно'''


def counter_words(word: str, list_of_words: list) -> int:
    counter = 0
    for element in list_of_words:
        if element == word:
            counter += 1
    return counter


def transformation_text(text: str) -> dict:
    text = text.lower()
    for i in range(len(text)):
        if text[i] in punctuation:
            text = text.replace(text[i], ' ')

    list_of_words = text.split()
    set_of_words = set(list_of_words)
    dict_of_count_words_tmp = {}.fromkeys(set_of_words, 0)
    for element in set_of_words:
        dict_of_count_words_tmp[element] = counter_words(element, list_of_words)

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
print(dict_of_count_words)