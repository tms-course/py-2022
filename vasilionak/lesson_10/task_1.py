"""Реализовать класс Context, который будет принимать обязательный аргумент expression
- это строка с математическим выражением. У класса также будет метод evaluate, в
котором нужно рекурсивно разобрать expression на составляющие и вернуть перефор-
матированное выражение, где числа будут обернуты в [x], а операторы с операндами
в (x*y):
ctx = Context("3*2 + 7^3")
print(ctx.evaluate())
# (([3] * [2]) + ([7] ^ [3]))"""


class Context:
    """:atribute op_map: list mathhematical operators"""
    op_map: list = ['+', '-', '/', '*', '^']
    def __init__(self, expression) -> None:
        """:param expression: expression for solve"""
        self.expression = expression

    @staticmethod
    def _eval(expression: str)->str:
        """Recursion method
        :returns: return wrapped expression: number wrapped in [], expression in ()"""
        prepared_expr = expression.strip()

        try:
            float(prepared_expr)
            return f'[{prepared_expr}]'
        except:
            pass

        for op in Context.op_map:
            
            if op not in prepared_expr:
                continue

            left_part, right_part = prepared_expr.split(op, 1)
                
            return f'({Context._eval(left_part)} {op} {Context._eval(right_part)})'

        

    def evaluate(self)-> str:
        """:return wrapped expression as a string"""
        return self._eval(self.expression)
    
ctx = Context("3*4 + 6^4")
print(ctx.evaluate())

        