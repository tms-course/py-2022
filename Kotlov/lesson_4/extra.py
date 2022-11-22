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

word_count = {i: our_text.count(i) for i in our_text}  # Создаём словарь элементами которого являются слова и их количество в тексте


def words_ranker(text_num: dict, count_n=0) -> str:
    """
    Печатает n строк встречающихся слов по порядку убывания кол-ва повторений этого слова в тексте.
    При одинаковом кол-ве вхождений слов, выводим первые k из них.
    """

    list_equal_count, list_equal_count_k = [], []   #  Cоздаём список со словами с одинаковым кол-во повторения
                                                    #  и список со словами с одинаковым кол-во повторения
                                                    #  + количество,которых не превосходит k

    maxi_n = 0  # Кол-во повторений слова в тексте

    if count_n == n:  # Проверка кол-ва выведенных строк с тем которое задали мы в начале(эта проверка стоит в начале,а
                      # не в конце,т.к, если мы введём n = 0,то всё полетит))
        return ''

    for key, value in text_num.items():  # Находим кол-во, самого часто встречаемого элемента
        if value > maxi_n:
            maxi_n = value

    for key, value in text_num.items():  # Находим слова,которые встречаюся maxi_n раз + проверяем сколько максимум таких слов может быть в строке
        if value == maxi_n:
            list_equal_count.append(key)

            if len(list_equal_count_k) < k:
                list_equal_count_k.append(key)

    print(maxi_n, end=' ')                  # Выводим наши строки, сначала кол-во повторений этих слов в тексте,а потом сами слова
    print(*list_equal_count_k, sep=', ')

    count_n += 1  # Cчитаем кол-во строк (уже выведенных)

    text_num = {key: value for key, value in text_num.items() if key not in list_equal_count}  # Убираем уже использованные элементы

    return None if text_num == {} else words_ranker(text_num, count_n)  # Если все слова выведены,то выходим из функции,иначе
                                                                # выполняем words_ranker() заново, до тех пор,
                                                                # пока у нас не останется не выведенных слов


words_ranker(word_count)
