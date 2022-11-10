import sys
from string import ascii_lowercase
from typing import List
from collections import defaultdict


CIRILIC_TEXT = ("Что тебе, что мне, что ей — всем нужно решить эту задачу "
"а что потом будет, потом и увидим, а увидим мы неприметно.")

ASCII_TEXT = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever "
"since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,"
"but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with"
"the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker"
"including versions of Lorem Ipsum")

CIRICIL_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


sys_args = sys.argv[1:]
try:
    num_of_most_often_words = int(sys_args[sys_args.index("-n") + 1])
    first_k_elements = int(sys_args[sys_args.index("-k") + 1])
except ValueError as err:
    print(f"{err}. Please provide argument")


def get_word(word: str) -> str:
    valid_chars = set((*CIRICIL_ALPHABET, *ascii_lowercase))
    invalid_chars = set(word) - valid_chars
    if invalid_chars:
        for char in invalid_chars:
            return word.replace(char, "")
    return word


def get_top_n_words(text: str, *, num_of_most_often_words: int, first_k_elements: int) -> List[str]:
    # Hashmap to count how frequently a word appears
    frequences = defaultdict(int)
    for word in text.split():
        correct_word = get_word(word.lower())
        if correct_word:
            frequences[correct_word] += 1

    # Hashmap to store frequency as a key
    words_by_frequency = defaultdict(list)
    for key, value in frequences.items():
        if len(words_by_frequency[value]) < first_k_elements:
            words_by_frequency[value].append(key)

    arr = []
    for count in range(max(words_by_frequency), 0, -1):
        if count in words_by_frequency:
            arr.append((count, words_by_frequency[count]))

    return [f"{count} {', '.join(words)}" for count, words in arr[:num_of_most_often_words]]


print(f"Result for ascii text with n={num_of_most_often_words} and k={first_k_elements}: ", 
      *get_top_n_words(ASCII_TEXT, num_of_most_often_words=num_of_most_often_words, first_k_elements=first_k_elements), sep="\n")
print(f"Result for cirilic text with n={num_of_most_often_words} and k={first_k_elements}: ", 
      *get_top_n_words(CIRILIC_TEXT, num_of_most_often_words=num_of_most_often_words, first_k_elements=first_k_elements), sep="\n")
