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
        return self.value


class NonTerminalExpression(AbstractExpression):
    """
    Class represents expression that includes arithmetical operators
    """
    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right

    def interpret(self):
        raise NotImplementedError


class Number(TerminalExpression):
    pass


class Add(NonTerminalExpression):
    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Sub(NonTerminalExpression):
    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class Mul(NonTerminalExpression):
    def interpret(self):
        return self.left.interpret() * self.right.interpret()


class Div(NonTerminalExpression):
    def interpret(self):
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            print('Division by zero error')
            raise SystemExit


class Pow(NonTerminalExpression):
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
            operator_position = expression_part.find(operator)
            left_part, right_part = None, None
            if operator_position != -1:
                left_part = self._evaluate(expression_part[:operator_position], )
                right_part = self._evaluate(expression_part[operator_position + 1:])
            else: continue
            match operator:
                case '+': return Add(left_part, right_part)
                case '-': return Sub(left_part, right_part)
                case '*': return Mul(left_part, right_part)
                case '/': return Div(left_part, right_part)
                case '^': return Pow(left_part, right_part)
        return Number(expression_part)

    def evaluate(self):
        """
        Interprets object returned from _evaluate method
        Returns: float number
        """
        return self._evaluate(self.expression).interpret()


c = Context('2*5 + 3^4')
print(c.evaluate())


