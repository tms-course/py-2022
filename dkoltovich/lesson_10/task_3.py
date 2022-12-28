import abc


class AbstractExpression:
    @abc.abstractmethod
    def interpret(self):
        """
        interprets expression string as float value
        :return: float result of expression
        """
        raise NotImplementedError


class TerminalExpression(AbstractExpression):
    """
        Class represents expression that does not include arithmetical operators
        """
    def __init__(self, value: str):
        self.value = float(value)

    def interpret(self):
        raise NotImplementedError


class NonTerminalExpression(AbstractExpression):
    """
    Class represents expression that includes arithmetical operators
    """
    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right

    def interpret(self):
        raise NotImplementedError




