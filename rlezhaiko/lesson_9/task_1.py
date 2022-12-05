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
        :param filepath: filepath
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
                returns = self.data_analyze(line.rstrip('\n'))
                list_of_returns.append(returns)
        return list_of_returns
    
    
    @staticmethod
    def data_analyze(data: str) -> tuple:
        """ 
        Data analyze function. If the total number of words
        greater than 10, the number of words with 2 or more "d" letters 
        does not exceed 2, and each "{" has "}", then the string is valid
        
        :returns: return tuple of boolean valid data and substring of data
        """
        flag_valid = False
        sub_str = data[:7]        
        list_index_opening_brackets, list_index_closing_brackets = [], []
        for i in range(len(data)):
            if data[i] == '{':
                list_index_opening_brackets.append(i)
            elif data[i] == '}':
                list_index_closing_brackets.append(i)
            
            if data[i] in punctuation:
                data = data.replace(data[i], ' ')
        
        words = data.split()
        words_with_more_one_d = list(filter(lambda x: x.count('d') == 2, words))
        
        if (len(words) > 10) and (len(words_with_more_one_d) >= 2):                
            if (len(list_index_opening_brackets) == len(list_index_closing_brackets)) and (len(list_index_closing_brackets) == 0):
                flag_valid = True
            elif (len(list_index_opening_brackets) == len(list_index_closing_brackets)):
                summ = 1
                for i in range(len(list_index_opening_brackets)):
                    if list_index_opening_brackets[i] > list_index_closing_brackets[i]:
                        summ *= 0
                        break
                flag_valid = bool(summ)
        
        return (flag_valid, sub_str)


path = 'data/text.txt'
ca = ContentAnalyzer(path)
print(ca.analyze())