""" 
1. #staticmethod
Создать класс ContentAnalyzer, который принимает filepath как параметр, и при вызове
метода anaslyze возвращает список из кортежей, где первый элемент говорит валидна
строка или нет, а второй - это первые 7 символов строки. Если общее количество слов,
больше 10, количество слов с 2-мя и более буквами "d" не превышает 2, и каждая "{" 
имеет "}", то строка валидна.
"""

class ContentAnalyzer(object):
    """
    Class ContentAnalyzer
    
    Creates an instance of a ContentAnalyzer class
    """
    def __init__(self, filepath: str) -> None:
        """ 
        :param filepath: filepath
        """
        self.filepath = filepath
    
    
    def analyze(self):
        """ 
        Analyze function
        
        Read file by filepath and send text to staticmethod data_analyze
        """
        with open(self.filepath, 'r') as f:
            data = f.read()
            returns = self.data_analyze(data)
            print(returns)
    
    
    @staticmethod
    def data_analyze(data: str) -> list:
        """ 
        Data analyze function (staticmethod)
        
        :returns: return list of tuples 
        """
        flag_valid, data, sub_str, list_tmp = False, data.strip(), '', []
        if len(data) > 7:
            sub_str = data[:7]
        
        words = data.split()
        words_with_more_one_d = list(filter(lambda x: x.count('d') == 2, words))
        if len(words) > 10:
            if data.count('{') == data.count('}'):
                if len(words_with_more_one_d) >= 2:
                    flag_valid = True
        
        tuple_tmp_1 = (flag_valid,)
        tuple_tmp_2 = (sub_str,)
        list_tmp.extend([tuple_tmp_1, tuple_tmp_2])
        return list_tmp


path = 'data/text.txt'
ca = ContentAnalyzer(path)
ca.analyze()