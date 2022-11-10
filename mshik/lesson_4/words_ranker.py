
import sys
from collections import defaultdict


CIRILIC_TEXT = ("Что тебе, что мне, что ей — всем нужно решить эту задачу "
"а что потом будет, потом и увидим, а увидим мы неприметно")

ASCII_TEXT = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever "
"since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,"
"but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with"
"the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker"
"including versions of Lorem Ipsum")


sys_args = sys.argv[1:]
try:
    n = int(sys_args[sys_args.index("-n") + 1])
    k = int(sys_args[sys_args.index("-k") + 1])
except ValueError as err:
    print(f"{err}. Please provide argument")


def get_top_n_words(text: str, *, n: int, k: int):
    # Hashmap to count how frequently a word appears
    frequences = defaultdict(int)
    words = [word.lower() for word in text.split() if word.isalpha()]
    for word in words:
        frequences[word] += 1

    # Hashmap to store frequency as a key
    words_by_frequency = defaultdict(list)
    for key, value in frequences.items():
        if len(words_by_frequency[value]) < k:
            words_by_frequency[value].append(key)

    arr = []
    for count in range(len(text), 0, -1):
        if count in words_by_frequency:
            arr.append((count, words_by_frequency[count]))

    return [f"{count} {', '.join(words)}" for count, words in arr[:n]]


print(f"Result for ascii text with n={n} and k={k}: ", *get_top_n_words(ASCII_TEXT, n=n, k=k), sep="\n")
print(f"Result for cirilic text with n={n} and k={k}: ", *get_top_n_words(CIRILIC_TEXT, n=n, k=k), sep="\n")
