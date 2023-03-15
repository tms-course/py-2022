"""
1. Реализовать класс Context, который будет принимать обязательный аргумент expression 
- это строка с математическим выражением. У класса также будет метод evaluate, в
котором нужно рекурсивно разобрать expression на составляющие и вернуть переформатированное выражение, 
где числа будут обернуты в [x], а операторы с операндами в (x*y).
"""


class Context:
    """
    Класс Context предназначен для обработки и вычисления математических выражений.
    """
    OPERATORS = ['+', '-', '*', '/', '^']

    def __init__(self, expression: str):
        """
        Инициализация контекста с заданным выражением.

        :param expression: строка, содержащая математическое выражение для вычисления.
        """
        self.expression = expression

    @staticmethod
    def validate_expression(expression) -> bool:
        """
        Валидация математического выражения.

        :param expression: строка, содержащая математическое выражение для проверки.
        :return: True, если выражение валидно, иначе False.
        """
        for char in expression:
            if char not in Context.OPERATORS and not char.isdigit() and char != ' ':
                return False
        return True

    def process_expression(self, expression_part: str) -> str:
        """
        Рекурсивная обработка частей математического выражения.

        :param expression_part: строка, содержащая часть математического выражения для обработки.
        :return: обработанная строка математического выражения.
        """
        expression_part = expression_part.strip()
        for operator in self.OPERATORS:
            operands = expression_part.split(operator, 1)
            if len(operands) > 1:
                left_operand = self.process_expression(operands[0])
                right_operand = self.process_expression(operands[1])
                return f'({left_operand} {operator} {right_operand})'
        return f'[{expression_part}]'

    def evaluate(self) -> str:
        """
        Вычисление математического выражения.

        :return: строка с результатом вычисления математического выражения.
        :raises ValueError: если выражение невалидно.
        """
        if not self.validate_expression(self.expression):
            raise ValueError('Expression is not valid')
        else:
            return self.process_expression(self.expression)

ctx = Context("3*2 + 7^3")
print(ctx.evaluate())
