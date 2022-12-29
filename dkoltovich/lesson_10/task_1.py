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
    def __init__(self, expression: str):
        """
        :param expression: expression needs to be evaluated
        """
        self.expression = expression

    def _evaluate(self, expression_part: str):
        """
        Recursion method that processes expression by operators
        :param expression_part: either part or full expression needs to be evaluated
        :return: string expression where numbers are covered in [] and operators with its operands are covered in ()
        """
        expression_part = expression_part.strip()
        for operator in ['+', '-', '*', '/', '^']:
            operator_position = expression_part.find(operator)
            left_part, right_part = None, None
            if operator_position != -1:
                left_part = self._evaluate(expression_part[:operator_position], )
                right_part = self._evaluate(expression_part[operator_position + 1:])
                return f'({left_part} {operator} {right_part})'
        return f'[{expression_part}]'

    def evaluate(self):
        return self._evaluate(self.expression)


c = Context('2*5 + 3^3')
print(c.evaluate())
