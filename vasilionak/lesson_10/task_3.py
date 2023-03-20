"""Ввести уровень абстракции в текущую реализацию добавив классы TerminalExpression с
обязательным аргументом value: float, представляющий значения, которые нельзя раз-
бить на части - это числа, класс Number должен быть унаследован от этого класса,
NonTerminalExpression с двумя обязательными аргументами left - левый операнд, right
- правый операнд, который будет представлять любое комплексное выражение, т.е все
классы операций Add, ..., Pow должны быть унаследованы от этого класса. И послед-
ним мы добавим класс AbstractExpression, который будет представлять любое выра-
жение в программе, и который будет иметь только один абстрактный метод(смотреть
@abc.abstractmethod) - interpret() возвращающий вычисленное значение float. Классы
TerminalExpression и NonTerminalExpression должны быть унаследованы от него."""

from __future__ import annotations

import abc


class CustomZeroDivsion(Exception):...

class AbstractExpression(abc.ABC):
    @abc.abstractclassmethod
    def interpret() -> float:...
 

class TerminalExpression(AbstractExpression):
    """:param value: value in float"""
    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
        """:returns: return value"""
        return self.value


class NonTerminalExpression(AbstractExpression):
    def __init__(self, left: AbstractExpression, right: AbstractExpression) -> None:
        self.left = left
        self.right = right


class Number(TerminalExpression):
    ...
    
class Add(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()


class Sub(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()


class Mul(NonTerminalExpression):
   def interpret(self)->float:
        return self.left.interpret() * self.right.interpret()
    

class Div(NonTerminalExpression):
    def interpret(self) -> float:
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            raise CustomZeroDivsion
        

class Pow(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() ** self.right.interpret()



class Context:
    """:atribute op_map: dict mathhematical operators"""
    op_map: dict = {'+': Add, 
                    '-': Sub, 
                    '/': Div, 
                    '*': Mul, 
                    '^': Pow}
    def __init__(self, expression) -> None:
        """:param expression: expression for solve"""
        self.expression = expression

    @staticmethod
    def _eval(expression: str)-> AbstractExpression:
        """Recursion method
        :returns: return wrapped expression: number wrapped in [], expression in ()"""
        prepared_expr = expression.strip()

        try:
            float(prepared_expr)
            return Number(float(prepared_expr))
        except:
            pass

        for op in Context.op_map:
            
            if op not in prepared_expr:
                continue

            left_part, right_part = prepared_expr.split(op, 1)
            left = Context._eval(left_part)
            right = Context._eval(right_part)
                
            return Context.op_map[op](left, right)

        

    def evaluate(self)-> AbstractExpression:
        """:return wrapped expression as a string"""
        return self._eval(self.expression)
    
ctx = Context("7/4 * 3^4")
expr = ctx.evaluate()
print(expr.interpret())