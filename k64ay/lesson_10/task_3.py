"""
Ввести уровень абстракции в текущую реализацию добавив классы TerminalExpression с обязательным аргументом value: float, 
который будет представлять любое конечное значение, т.е значение, которое нельзя разбить на части - это числа, 
на данный момент только Number должен быть унаследовать от этого класса,
NonTerminalExpression с двумя обязательными аргументами left - левый операнд, right - правый операнд, который будет представлять
любое комплексное выражение, т.е все классы операций Add, ..., Pow должны быть унаследованы от этого класса.
И последним мы добавим класс AbstractExpression, который будет представлять вообще любое выражение в программе, 
и который будет иметь только один абстрактный метод(смотреть @abc.abstractmethod) - interpret() возвращающий вычисленное значение float.
Классы TerminalExpression и NonTerminalExpression должны быть унаследованы от него.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

line = "3*2 + 7^3 + 10 - 5/2"


class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self) -> float:
        raise NotImplementedError


class TerminalExpression(AbstractExpression):
    def __init__(self, value: float):
        self.value = value


class NonTerminalExpression(AbstractExpression):
    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right


class Number(TerminalExpression):
    def interpret(self) -> float:
        return self.value


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
    op_order_map = {
        '+': Add, 
        '-': Sub, 
        '*': Mul, 
        '/': Div, 
        '^': Pow,
    }

    def __init__(self, expression: str):
        self.expression = expression
        self.op_order = list(self.op_order_map.keys())

    def __eval(self, expression) -> AbstractExpression:
        expr = expression.strip()


        if not any(op in expr for op in self.op_order):
            return Number(float(expr))

        for op in self.op_order:
            if op not in expr:
                continue
            
            sub_exprs = expr.split(op, 1)
            left = self.__eval(sub_exprs[0])
            right = self.__eval(sub_exprs[1])

            return self.op_order_map[op](left, right)


    def evaluate(self) -> AbstractExpression:
        return self.__eval(self.expression)


ctx = Context(line)
ex: AbstractExpression = ctx.evaluate(line)
print(ex.interpret())

