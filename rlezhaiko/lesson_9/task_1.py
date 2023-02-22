""" 
1. #staticmethod
Создать класс ContentAnalyzer, который принимает filepath как параметр, и при вызове
метода anaslyze возвращает список из кортежей, где первый элемент говорит валидна
строка или нет, а второй - это первые 7 символов строки. Если общее количество слов,
больше 10, количество слов с 2-мя и более буквами "d" не превышает 2, и каждая "{" 
имеет "}", то строка валидна.
"""
from string import punctuation


class ContentAnalyzer(object):
    """
    Creates an instance of a ContentAnalyzer class
    """
    def __init__(self, filepath: str) -> None:
        """ 
        :param filepath: relative path to file
        """
        self.filepath = filepath
    
    
    def analyze(self) -> list:
        """ 
        Read file by filepath line by line and send text to staticmethod data_analyze
        
        :returns: return list of tuples
        """
        list_of_returns = []
        with open(self.filepath, 'r') as f:
            for line in f:
                returns = self.data_analyze(line)
                list_of_returns.append(returns)
        return list_of_returns
    
    
    @staticmethod
    def data_analyze(data: str) -> tuple:
        """ 
        If the total number of words greater than 10, the number of words with 2 
        or more "d" letters does not exceed 2, and each "{" has "}", then the string is valid
        
        :param data: string for analyze
        :returns: return tuple of boolean valid data and substring of data
        """
        data = data.rstrip('\n')
        # flag_valid = False
        sub_str = data[:7]
        if not ContentAnalyzer.check_brackets(data):
            return (False, sub_str)

        for i in range(len(data)):
            if data[i] in punctuation:
                data = data.replace(data[i], ' ')

        words = data.split()
        if len(words) < 10:
            return (False, sub_str)

        words_with_more_one_d = list(filter(lambda x: x.count('d') == 2, words))
        if len(words_with_more_one_d) < 2:
            return (False, sub_str)
        
        return (True, sub_str)
    

    @staticmethod
    def check_brackets(data: str) -> bool:
        """ 
        Check data for valid brackets where each "{" has "}", then the string is valid

        :param data: string for analyze
        :returns: return True if string is valid for brackets, False otherwise
        """
        counter = 0
        for i in data:
            if i == '{':
                counter += 1
            elif i == '}':
                counter -= 1

            if counter == -1:
                break
        
        return counter == 0


path = 'data/text.txt'
ca = ContentAnalyzer(path)
print(ca.analyze())