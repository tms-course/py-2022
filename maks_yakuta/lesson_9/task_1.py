"""
Задание 1.
Создать класс ContentAnalyzer, который принимает filepath(путь к файлу) как параметр,
и при вызове обычного метода analyze происходит чтение файла, путь которого
мы указали в конструкторе, и возвращается список из картежей, где первый элемент
говорит валидна строка или нет, а второй - это первые 7 символов строки.
«Eсли общее количество слов, больше 10, колличество слов с 2-мя и более буквами "d" не превышает 2,
и каждая "{" имеет "}", то строка валидна » <- это сделать статическим методо.
"""


class ContentAnalyzer:

    def __init__(self, file_path: str):

        self.file_path = file_path

    def analyze(self):

        list_tuples = []
        with open('file.txt', "r") as file:
            for line in file:
                is_valid = ContentAnalyzer.is_valid(line)
                list_tuples.append((is_valid, line[:7]))

        return list_tuples

    @staticmethod
    def is_valid(line: str):

        list_words = line.split()
        if len(list_words) <= 10:
            return False
        open_brackets = 0
        words_with_two_d = 0
        for word in list_words:
            if word.count('d') >= 2:
                words_with_two_d += 1
                if words_with_two_d > 2:
                    return False
            if '{' in word:
                open_brackets += 1
            elif '}' in word:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    return False
        else:
            is_valid_brackets = open_brackets == 0

        return (words_with_two_d <= 2
                and len(list_words) > 10
                and is_valid_brackets)


Analysis = ContentAnalyzer('file.txt')
print(Analysis.analyze())