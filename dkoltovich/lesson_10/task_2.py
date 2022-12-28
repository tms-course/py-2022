class Number:
    def __init__(self, value: str):
        self.value = float(value)

    def interpret(self):
        return self.value


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Sub:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()


class Div:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            print('Division by zero error')
            raise SystemExit


class Pow:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() ** self.right.interpret()


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
            operator_pos, left_part, right_part = self.process_operator(expression_part, operator)
            if operator_pos == -1: continue
            match operator:
                case '+': return Add(left_part, right_part)
                case '-': return Sub(left_part, right_part)
                case '*': return Mul(left_part, right_part)
                case '/': return Div(left_part, right_part)
                case '^': return Pow(left_part, right_part)
        return Number(expression_part)

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


c = Context('2*5 + 3^4')
print(c.evaluate())