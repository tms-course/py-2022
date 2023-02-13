"""
1.
Создать класс ContentAnalyzer, который принимает filepath(путь к файлу) как параметр,
и при вызове обычного метода analyze происходит чтение файла, путь которого мы указали в конструкторе,
и возвращается список из кортежей, где первый элемент говорит валидна строка или нет,
а второй - это первые 7 символов строки.
« Eсли общее количество слов, больше 10, колличество слов с 2-мя и более буквами "d" не превышает 2,
и каждая "{" имеет "}", то строка валидна » <- это сделать статическим методом.
"""


class ContentAnalyzer:
    """
    The class used to analyze the file.
    Class Attributes:
        str file_path: the path to the file for analysis.
    """

    def __init__(self, file_path: str):
        """
        :param str file_path: analyzes the file by this path
        """
        self.file_path = file_path

    def analyze(self):
        """
        Method for class analysis
        :return: a list of tuples is returned, where the first element says whether the string is valid or not, and
        the second is the first 7 characters of the string
        """
        tuple_list = []
        with open(self.file_path, "r") as file:
            for line in file:
                valid_line = ContentAnalyzer.valid_line(line)
                tuple_list.append((valid_line, line[:7]))
        return tuple_list

    @staticmethod
    def valid_line(line: str):
        """
        Check the string for validity
        :param line: string analyze
        :return: True if line valid and False in other cases
        """
        line_words = line.split()
        if len(line_words) <= 10:
            return False
        words_with_d = 0
        brace_in_line = 0
        for word in line_words:
            if word.count('d') >= 2:
                words_with_d += 1
                if words_with_d > 2:
                    return False
            if '{' in word:
                brace_in_line += 1
            elif '}' in word:
                if brace_in_line > 0:
                    brace_in_line -= 1
                else:
                    return False
        else:
            brace_in_line_valid = brace_in_line == 0

        return words_with_d <= 2 and len(line_words) > 10 and brace_in_line_valid


Analysing = ContentAnalyzer('./TMS_content.txt')
print(Analysing.analyze())
