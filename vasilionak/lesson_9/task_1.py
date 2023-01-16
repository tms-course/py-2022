"""Создать класс ContentAnalyzer, который принимает filepath(путь к файлу) как пара-
метр, и при вызове обычного метода analyze происходит чтение файла, путь которого
мы указали в конструкторе, и возвращается список из картежей, где первый элемент
говорит валидна строка или нет, а второй - это первые 7 символов строки. « Eсли общее
количество слов, больше 10, колличество слов с 2-мя и более буквами "d" не превышает
2, и каждая "{" имеет "}", то строка валидна » <- это сделать статическим методом."""

class ContentAnalyzer(object):
    """
    A classed used to represent a ContentAnalyzer
        Attributes:
        filepath: str, path to file need to be analyzed
    """
    def __init__(self, filepath: str):
        """
        :param filepath: file for analyze
        """
        self.filepath = filepath
 
        
    @staticmethod
    def is_line_valide(line) -> bool:
        """
        Check file for valid
        :param: string for analyze
        :return: True if line is vslid, False otherwise 
        """
        words = line.split()
        if len(words) <= 10:
            return False

        words_with_dd = list(filter(lambda x: x.count('d') == 2, words))
        if len(words_with_dd) <= 2:
            return False

        return True


    @staticmethod
    def valid_brackets(line) -> bool:
        """
        Check line for valid brackets
        :param: string for analyze
        :return: True if line is valid for brackets and False if not
        """
        counter = 0
        for i in line:
            if i == '{':
                counter += 1
            elif i == '}':
                counter -= 1
            if counter == -1:
                break
        return counter == 0


    def analyze(self):
        """
        Analyze file
        :return: list of typles, where the first elemnt says is string valid,
        and second - first 7 chars in line
        """
        list_of_result = []
        with open(self.filepath, 'r') as f:
            for line in f:
                valid_line = self.is_line_valide(line)
                if self.is_line_valide(line) == True:
                    valid_line = self.valid_brackets(line)
                    list_of_result.append((valid_line, line[:7]))

