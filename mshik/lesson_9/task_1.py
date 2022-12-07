"""
Задание 1.

Создать класс ContentAnalyzer, который принимает filepath(путь к файлу) как параметр, 
и при вызове обычного метода analyze происходит чтение файла, путь которого
мы указали в конструкторе, и возвращается список из картежей, где первый элемент
говорит валидна строка или нет, а второй - это первые 7 символов строки. 
«Eсли общее количество слов, больше 10, колличество слов с 2-мя и более буквами "d" не превышает 2, 
и каждая "{" имеет "}", то строка валидна » <- это сделать статическим методом.
"""
from typing import List, Tuple


class ContentAnalyzer:
    """
    A classed used to represent a ContentAnalyzer

    Attributes:
        filepath (str): Path to file, which need to be analyzed

    Methods:
        is_valid_brackets(line): Checks if brackets in the right order
        get_validated_line(line): Returns a tuple of is_valid string and first 7 chars
        analyze(): Returns a list of tuples, where tuples are validated lines
    """
    def __init__(self, filepath: str) -> None:
        """
        Args:
            filepath (str): Path to file, which need to be analyzed
        """
        self.filepath = filepath

    @staticmethod
    def is_valid_brackets(line: str) -> bool:
        """
        Checks if brackets in the right order

        Args:
            line (str): line which need to be validated on brackets

        Returns:
            bool: True if stack is empty else False
        """
        stack = []
        open_bracket, close_bracket = "{", "}"
        for char in line:
            if char not in (open_bracket, close_bracket):
                continue
            elif char == open_bracket:
                stack.append(char)
            elif len(stack) > 0:
                if stack.pop() != open_bracket:
                    return False
            else:
                return False

        return len(stack) == 0
    
    @staticmethod
    def is_line_valid(line: str) -> bool:
        """
        Returns a bool if string is valid.

        Args:
            line(str): line which need to be analyzed
        
        Returns:
            bool: True if string is valid otherwise False  
        """
        splited_line = line.split()
        words_with_double_d = [word for word in splited_line if word.count("d") >= 2]
        return len(splited_line) > 10 and len(words_with_double_d) <= 2 and ContentAnalyzer.is_valid_brackets(line)
    
    def analyze(self) -> List[Tuple[bool, str]]:
        """
        Analyzes lines in file

        Returns:
            List[Tuple[bool, str]]: List of tuples, where tuples are validated lines"""
        with open(self.filepath, "r") as file:
            validated_lines = []
            for line in file.readlines():
                line = line.strip()
                validated_line = self.is_line_valid(line)
                validated_lines.append((validated_line, line[:7]))
            return validated_lines


content_analyzer = ContentAnalyzer("./data/lorem_ipsum.txt")
print(content_analyzer.analyze())