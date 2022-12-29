"""
task 1:
Реализовать класс Context, который будет принимать обязательный аргумент expression
- это строка с математическим выражением. У класса также будет метод evaluate, в
котором нужно рекурсивно разобрать expression на составляющие и вернуть перефор-
матированное выражение, где числа будут обернуты в [x], а операторы с операндами
в (x*y):
ctx = Context("3*2 + 7^3")
print(ctx.evaluate())
# (([3] * [2]) + ([7] ^ [3]))
"""


class Context:
    """
    Attributes:
        operators: list - operators that could be included in expression
    """
    operators = ['+', '-', '*', '/', '^']

    def __init__(self, expression: str):
        """
        :param expression: expression needs to be evaluated
        """
        self.expression = expression

    def is_expression_valid(self, expression) -> bool:
        """
        Checks if expression includes only numbers, spaces and operators (+, -, *, /, ^)
        Returns: True if expression is valid, False otherwise

        """
        for char in expression:
            if char not in self.operators and not char.isdigit() and char != ' ':
                return False
        return True

    def _evaluate(self, expression_part: str) -> str:
        """
        Recursion method that processes expression by operators
        :param expression_part: either part or full expression needs to be evaluated
        :return: string expression where numbers are covered in [] and operators with its operands are covered in ()
        """
        expression_part = expression_part.strip()
        for operator in self.operators:
            operands = expression_part.split(operator, 1)
            if len(operands) > 1:
                left_part = self._evaluate(operands[0])
                right_part = self._evaluate(operands[1])
                return f'({left_part} {operator} {right_part})'
        return f'[{expression_part}]'

    def evaluate(self) -> str:
        if not self.is_expression_valid(self.expression):
            print('Expression is not valid')
        else:
            return self._evaluate(self.expression)


c = Context('2*5 + 3 + 3^3')
print(c.evaluate())
