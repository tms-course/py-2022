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
    operators = ['+', '-', '*', '/', '^']


    def __init__(self, expression: str):
        self.expression = expression

    def _evaluate(self, expression_part: str) -> str:
        expression_part = expression_part.strip()
        for operator in self.operators:
            operands = expression_part.split(operator, 1)
            if len(operands) > 1:
                left_part = self._evaluate(operands[0])
                right_part = self._evaluate(operands[1])
                return f'({left_part} {operator} {right_part})'
        return f'[{expression_part}]'


    def evaluate(self) -> str:
        return self._evaluate(self.expression)


ctx = Context("4+2 * 2+3")
print(ctx.evaluate())