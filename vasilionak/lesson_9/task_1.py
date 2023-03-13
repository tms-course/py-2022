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
    def __init__(self, filepath: str) -> None:
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
        
        dd_word_count = 0
        for word in words:
            if word.cont('d') >= 2:
                dd_word_count += 1

                if dd_word_count > 2:
                    return False

        return ContentAnalyzer.valid_brackets(line)


    @staticmethod
    def valid_brackets(line) -> bool:
        """
        Check line for valid brackets
        :param: string for analyze
        :return: True if line is valid for brackets and False if not
        """
        bracket_count = 0
        for ch in line:
            if ch == '{':
                bracket_count += 1
            elif ch == '}':
                bracket_count -= 1

            if bracket_count < 0:
                return False
            
        return bracket_count == 0


    def analyze(self)-> list[tuple]:
        """
        Analyze file
        :return: list of typles, where the first elemnt says is string valid,
        and second - first 7 chars in line
        """
        result = []
        with open(self.filepath, 'r') as file:
            for line in file:
                result.append((self.is_line_valide(line), line[:7]))

        return result   

           