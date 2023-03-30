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
        raise NotImplementedError


class TerminalExpression(AbstractExpression):
    def __init__(self, value: float):
        self.value = value

    def interpret(self) -> float:
        return self.value


class NonTerminalExpression(AbstractExpression):
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
        return self.left.interpret() / self.right.interpret()

class Pow(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() ** self.right.interpret()


class Context:

    operators = ['+', '-', '*', '/', '^']
    op_class = {'+': Add,
                '-': Sub,
                '*': Mul,
                '/': Div,
                '^': Pow
    }

    def __init__(self, expression: str):
        self.expression = expression



    def _evaluate(self, expression_part: str) -> AbstractExpression:
        expression_part = expression_part.strip()
        for operator in self.operators:
            operands = expression_part.split(operator, 1)
            if len(operands) > 1:
                left_part = self._evaluate(operands[0])
                right_part = self._evaluate(operands[1])
                return self.op_class[operator](left_part, right_part)
        return Number(float(expression_part))

    def evaluate(self) -> AbstractExpression:
        return self._evaluate(self.expression)


ctx = Context('3*3 + 9^3')
expr = ctx.evaluate()
print(expr.interpret())

