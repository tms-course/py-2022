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
        __init__ function
        
        :param self: self object of class
        :param filepath: filepath
        :returns: return None 
        """
        self.filepath = filepath
    
    
    @staticmethod
    def analyze(filepath: str) -> list:
        """ 
        Analyze function (staticmethod)
        
        :param self: self object of class
        :returns: return list of tuples 
        """
        flag_valid, filepath, sub_str, list_tmp = False, filepath.strip(), '', []
        if len(filepath) > 7:
            sub_str = filepath[:7]
        
        words = filepath.split()
        words_with_more_one_d = list(filter(lambda x: x.count('d') == 2, words))
        if len(words) > 10:
            if filepath.count('{') == filepath.count('}'):
                if len(words_with_more_one_d) >= 2:
                    flag_valid = True
       
        list_tmp.insert(0, flag_valid)
        list_tmp.append(sub_str)
        return list_tmp


path = 'aa bb cc dd ff ee gg hh jj {} dd'
lst = ContentAnalyzer.analyze(path)
if lst[0]:
    print(f'Path valid: {lst[0]}')
    c = ContentAnalyzer(path) 
else:
    print(f'Path valid: {lst[0]}')