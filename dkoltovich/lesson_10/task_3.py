import abc


class AbstractExpression:
    @abc.abstractmethod
    def interpret(self):
        return TerminalExpression(NonTerminalExpression)


class TerminalExpression(AbstractExpression):
    def __init__(self, value):
        self.value = float(value)


class NonTerminalExpression(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right



