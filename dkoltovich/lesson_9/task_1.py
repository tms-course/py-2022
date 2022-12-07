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
        """
        :param str file_path: path to the file needs to be analysed
        """
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
                is_valid = ContentAnalyzer.is_valid(line)
                list_of_tuples.append((is_valid, line[:7]))

        return list_of_tuples

    @staticmethod
    def is_valid(line: str):
        """
        Checks if string is valid
        :param line: string needs to be analyzed
        :return: True if line is valid, False otherwise
        """
        list_of_words_in_line = line.split()
        if len(list_of_words_in_line) <= 10:
            return False
        amount_of_open_brackets = 0
        amount_of_words_with_two_d = 0
        for word in list_of_words_in_line:
            if word.count('d') >= 2:
                amount_of_words_with_two_d += 1
                if amount_of_words_with_two_d > 2: return False
            if '{' in word:
                amount_of_open_brackets += 1
            elif '}' in word:
                if amount_of_open_brackets > 0:
                    amount_of_open_brackets -= 1
                else:
                    return False
        else:
            is_valid_brackets = amount_of_open_brackets == 0

        return (amount_of_words_with_two_d <= 2
                and len(list_of_words_in_line) > 10
                and is_valid_brackets)


analyzer = ContentAnalyzer('./content.txt')
print(analyzer.analyze())





