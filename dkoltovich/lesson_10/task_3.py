"""
task 3:
Ввести уровень абстракции в текущую реализацию добавив классы TerminalExpression с
обязательным аргументом value: float, представляющий значения, которые нельзя раз-
бить на части - это числа, класс Number должен быть унаследован от этого класса,
NonTerminalExpression с двумя обязательными аргументами left - левый операнд, right
- правый операнд, который будет представлять любое комплексное выражение, т.е все
классы операций Add, ..., Pow должны быть унаследованы от этого класса. И послед-
ним мы добавим класс AbstractExpression, который будет представлять любое выра-
жение в программе, и который будет иметь только один абстрактный метод(смотреть
@abc.abstractmethod) - interpret() возвращающий вычисленное значение float. Классы
TerminalExpression и NonTerminalExpression должны быть унаследованы от него.
"""
import abc


class AbstractExpression:
    @abc.abstractmethod
    def interpret(self) -> float:
        """
        interprets expression string as float value
        :return: float result of expression
        """
        raise NotImplementedError


class TerminalExpression(AbstractExpression):
    """
    Class represents expression that does not include arithmetical operators
    """
    def __init__(self, value: float):
        self.value = value

    def interpret(self) -> float:
        return self.value


class NonTerminalExpression(AbstractExpression):
    """
    Class represents expression that includes arithmetical operators
    """
    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        raise NotImplementedError


class Number(TerminalExpression):
    pass


class Add(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()


class Sub(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()


class Mul(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() * self.right.interpret()


class Div(NonTerminalExpression):
    def interpret(self) -> float:
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            print('Division by zero error')
            raise SystemExit


class Pow(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() ** self.right.interpret()


class Context:
    """
    Attributes:
        operators: list - operators that could be included in expression
        operation_class: dict - key is operator and value is its class
     """

    operators = ['+', '-', '*', '/', '^']
    operation_class = {'+': Add,
                       '-': Sub,
                       '*': Mul,
                       '/': Div,
                       '^': Pow
                       }

    def __init__(self, expression: str):
        """
        :param expression: expression needs to be evaluated
        """
        self.expression = expression

    def is_expression_valid(self, expression) -> bool:
        """
        Checks if expression includes only numbers, spaces and operators (+, -, *, /, ^)
        Returns: True if expression is valid, False otherwise

        """
        for char in expression:
            if char not in self.operators and not char.isdigit() and char != ' ':
                return False
        return True

    def _evaluate(self, expression_part: str) -> AbstractExpression:
        """
        Recursion method that processes expression by operators
        :param expression_part: either part or full expression needs to be evaluated
        :return: Abstract expression:
            TerminalExpression (Number) on the top of recursion stack,
            NonTerminalExpression will be returned as result
        """
        expression_part = expression_part.strip()
        for operator in self.operators:
            operands = expression_part.split(operator, 1)
            if len(operands) > 1:
                left_part = self._evaluate(operands[0])
                right_part = self._evaluate(operands[1])
                return self.operation_class[operator](left_part, right_part)
        return Number(float(expression_part))

    def evaluate(self) -> AbstractExpression:
        """
        Interprets object returned from _evaluate method
        Returns: float number
        """
        if not self.is_expression_valid(self.expression):
            print('Expression is not valid')
        else:
            return self._evaluate(self.expression)


c = Context('2*5 + 3^4')
print(c.evaluate().interpret())


