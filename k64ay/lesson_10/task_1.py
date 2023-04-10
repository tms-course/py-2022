class Context:
    op_map: list = ['+', '-', '/', '*', '^']

    def __init__(self, expression: str) -> None:
        self.expression = expression

    @staticmethod
    def _eval(expression: str) -> str:
        prepared_expr = expression.strip()
        print(prepared_expr)

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


    def evaluate(self) -> str:
        return self._eval(self.expression)
    
ctx = Context('3*2 + 7^3')
print(ctx.evaluate())