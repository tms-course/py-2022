from __future__ import annotations

import abc

class CustomZeroDivision(Exception): ...

class AbstractExpression(abc.ABC):
    @abc.abstractmethod
    def interpret() -> float: ...

class TerminalExpression(AbstractExpression):
    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
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
    def interpret(self) -> float:
        return self.left.interpret() * self.right.interpret()
    

class Div(NonTerminalExpression):
    def interpret(self) -> float:
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            raise CustomZeroDivision
    

class Pow(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() ** self.right.interpret()


class Context:
    op_map: dict = {
        '+': Add, 
        '-': Sub, 
        '/': Div, 
        '*': Mul, 
        '^': Pow,
    }

    def __init__(self, expression: str) -> None:
        self.expression = expression

    @staticmethod
    def _eval(expression: str) -> AbstractExpression:
        prepared_expr = expression.strip()

        try:
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


    def evaluate(self) -> AbstractExpression:
        return self._eval(self.expression)
    
ctx = Context('3*2 + 7^3 + 10 - 22^2')
expr = ctx.evaluate()
print(expr.interpret())