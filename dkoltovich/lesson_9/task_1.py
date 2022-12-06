"""
Задание 1.
Создать класс ContentAnalyzer, который принимает filepath(путь к файлу) как параметр,
и при вызове обычного метода analyze происходит чтение файла, путь которого
мы указали в конструкторе, и возвращается список из картежей, где первый элемент
говорит валидна строка или нет, а второй - это первые 7 символов строки.
«Eсли общее количество слов, больше 10, колличество слов с 2-мя и более буквами "d" не превышает 2,
и каждая "{" имеет "}", то строка валидна » <- это сделать статическим методом.
"""


class ContentAnalyzer:
    """
        A class used to represent a ContentAnalyzer
        Attributes:
            str file_path : Path to file need to be analyzed
        """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def analyze(self):
        """
        Method that analyze the file
        :return: list of tuples, where the first element says is string valid, and the second is first
            7 chars in each line
        """
        list_of_tuples = []
        with open(self.file_path, "r") as file:
            for line in file:
                if ContentAnalyzer.is_valid(line):
                    list_of_tuples.append(('valid', line[:7:]))
                else:
                    list_of_tuples.append(('not valid', line[:7:]))

        return list_of_tuples

    @staticmethod
    def is_valid(line: str):
        """
        Checks if string is valid
        :param line: string needs to be analyzed
        :return: True if line is valid, False otherwise
        """
        list_of_words_in_line = line.split()
        amount_of_words_with_two_d = len(list(filter(lambda x: x.count('d') >= 2, list_of_words_in_line)))
        return amount_of_words_with_two_d <= 2 \
               and len(list_of_words_in_line) > 10\
               and line.count('{') == line.count('}')


analyzer = ContentAnalyzer('./content.txt')
print(analyzer.analyze())





