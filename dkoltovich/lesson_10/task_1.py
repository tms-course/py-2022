import task_2 as operation


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
        operator_pos, left_part, right_part = self.process_operator(expression_part, '+')
        if operator_pos != -1:
            return operation.Add(left_part, right_part)

        operator_pos, left_part, right_part = self.process_operator(expression_part, '-')
        if operator_pos != -1:
            return operation.Sub(left_part, right_part)

        operator_pos, left_part, right_part = self.process_operator(expression_part, '*')
        if operator_pos != -1:
            return operation.Mul(left_part, right_part)

        operator_pos, left_part, right_part = self.process_operator(expression_part, '/')
        if operator_pos != -1:
            return operation.Div(left_part, right_part)

        operator_pos, left_part, right_part = self.process_operator(expression_part, '^')
        if operator_pos != -1:
            return operation.Pow(left_part, right_part)

        return operation.Number(expression_part)

    def process_operator(self, expression_part: str, operator: str):
        """
        Finds operator in the expression, then call _evaluate() for both left and right parts of expression
        :param expression_part: part or full expression
        :param operator: arithmetical operator to find and process
        :return: position of operator, left evaluated substring, right evaluated substring
        """
        operator_position = expression_part.find(operator)
        left_part, right_part = None, None
        if operator_position != -1:
            left_part = self._evaluate(expression_part[:operator_position], )
            right_part = self._evaluate(expression_part[operator_position + 1:])
        return operator_position, left_part, right_part

    def evaluate(self):

        return self._evaluate(self.expression).interpret()


c = Context('2*5 + 3^3')
print(c.evaluate())
