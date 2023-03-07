from __future__ import annotations


class ContentAnalyzer:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    @staticmethod
    def validate_brackets(line: str) -> bool:
        bracket_count = 0

        for ch in line:
            if ch == '{':
                bracket_count += 1
            elif ch == '}':
                bracket_count -= 1

            if bracket_count < 0:
                return False
        
        return bracket_count == 0

    @staticmethod
    def validate_line(line: str) -> bool:
        words = line.split()

        if len(words) <= 10:
            return False
        
        dd_word_count = 0
        for word in words:
            if word.count('d') >= 2:
                dd_word_count += 1

            if dd_word_count > 2:
                return False
            
        return ContentAnalyzer.validate_brackets(line)


    def analyze(self) -> list[tuple]:
        result = []

        with open(self.filepath, 'r') as file:
            for line in file:
                result.append((self.validate_line(line), line[:7]))

        return result
        