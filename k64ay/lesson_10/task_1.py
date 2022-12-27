"""
Реализовать класс Context, который будет принимать обязательный аргумент expression - это строка с математическим выражением.
У класса также будет метод evaluate, в котором нужно рекурсивно разобрать expression на составляющие и вернуть переформатированное
выражение, где числа будут обернуты в [x], а операторы с операндами в (x*y):
3*2 + 7^3 -> (([3] * [2]) + ([7] ^ [3]))
"""

line = "3*2 + 7^3 + 10 - 5/0"


class Context:
    op_order = ['+', '-', '*', '/', '^']

    def __init__(self, expression: str):
        self.expression = expression

    def __eval(self, expression: str) -> float:
        expr = expression.strip()

        if not any(op in expr for op in self.op_order):
            return f'[{expr}]'

        for op in self.op_order:
            if op not in expr:
                continue
            
            sub_exprs = expr.split(op, 1)
            return f'({self.evaluate(sub_exprs[0])} {op} {self.evaluate(sub_exprs[1])})'

    def evaluate(self) -> str:
        return self.__eval(self.expression)

ctx = Context(line)
print(ctx.evaluate())

