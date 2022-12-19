import task_2 as op


class Context:
    def __init__(self, expression: str):
        self.expression = expression

    def _evaluate(self, expression_part : str):
        expression_part = expression_part.strip()
        res = ''
        sign = '+'
        pos_sing = expression_part.find(sign)
        if pos_sing != -1:
            left_part = self._evaluate(expression_part[:pos_sing], )
            right_part = self._evaluate(expression_part[pos_sing + 1:])
            return op.Add(left_part, right_part).interpret()
        sign = '-'
        pos_sing = expression_part.find(sign)
        if pos_sing != -1:
            left_part = self._evaluate(expression_part[:pos_sing], )
            right_part = self._evaluate(expression_part[pos_sing + 1:])
            return op.Sub(left_part, right_part).interpret()
        sign = '*'
        pos_sing = expression_part.find(sign)
        if pos_sing != -1:
            left_part = self._evaluate(expression_part[:pos_sing], )
            right_part = self._evaluate(expression_part[pos_sing + 1:])
            return op.Mul(left_part, right_part).interpret()
        sign = '/'
        pos_sing = expression_part.find(sign)
        if pos_sing != -1:
            left_part = self._evaluate(expression_part[:pos_sing], )
            right_part = self._evaluate(expression_part[pos_sing + 1:])
            return op.Div(left_part, right_part).interpret()
        sign = '^'
        pos_sing = expression_part.find(sign)
        if pos_sing != -1:
            left_part = self._evaluate(expression_part[:pos_sing], )
            right_part = self._evaluate(expression_part[pos_sing + 1:])
            return op.Pow(left_part, right_part).interpret()

        return op.Number(expression_part)

    def evaluate(self):
        return self._evaluate(self.expression)


c = Context('2+5')
print(c.evaluate())