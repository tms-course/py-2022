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
        :return: Abstract expression:
            TerminalExpression (Number) on the top of recursion stack,
            NonTerminalExpression will be returned as result
        """
        expression_part = expression_part.strip()
        for operator in ['+', '-', '*', '/', '^']:
            operator_position = expression_part.find(operator)
            left_part, right_part = None, None
            if operator_position != -1:
                left_part = self._evaluate(expression_part[:operator_position], )
                right_part = self._evaluate(expression_part[operator_position + 1:])
            if operator_position == -1: continue
            match operator:
                case '+': return Add(left_part, right_part)
                case '-': return Sub(left_part, right_part)
                case '*': return Mul(left_part, right_part)
                case '/': return Div(left_part, right_part)
                case '^': return Pow(left_part, right_part)
        return Number(expression_part)

    def evaluate(self):

        return self._evaluate(self.expression).interpret()

c = Context('2*5 + 3^3')
print(c.evaluate())
