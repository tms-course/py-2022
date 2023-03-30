"""
task 2:
Расширить функционал, добавив класс Number, с обязательным аргументом - value,
который будет представлять любое число в выражениях, а также классы Add(сумма),
Sub(разность), Mul(умножение), Div(деление), Pow(степень) - которые представляют
все возможные операции, и принимают два обязательных аргумента left - левый опе-
ранд, right - правый операнд, операндом может быть любой объект выше перечисленных
классов. У всех упомянутых классов должен быть метод interpret(), который будет воз-
вращать вычисленное значение типа float(к примеру "4".interpret() -> 4, "3*2".interpret()
-> 6). Все исключительные ситуации отловить try/except блоками. Также нужно изме-
нить реализацию метода Context.evaluate() так, чтобы он возвращал не строку, а объект
одного из выше указанных классов. Обязательно указывать аннотации и пользоваться
только описанными классами.
ctx = Context("3*2 + 7^3")
print(ctx.evaluate())
# 349
"""
from __future__ import annotations

class DivisionByZero(Exception):
    pass

class Number:

    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
        return self.value

class Add:

    def __init__(self,
                left: Add | Sub | Mul | Div | Pow | Number,
                right: Add | Sub | Mul | Div | Pow | Number
    ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()

class Sub:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number
    ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()

class Mul:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number
    ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() * self.right.interpret()

class Div:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number
    ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() / self.right.interpret()


class Pow:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number
    ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() ** self.right.interpret()

class Context:
    operators = ['+', '-', '*', '/', '^']
    op_class = {'+': Add,
                '-': Sub,
                '*': Mul,
                '/': Div,
                '^': Pow,
    }

    def __init__(self, expression: str):
        self.expression = expression

    def _evaluate(self, expression_part: str)-> Add | Sub | Mul | Div | Pow | Number:
        expression_part = expression_part.strip()
        for operator in self.operators:
            operands = expression_part.split(operator, 1)
            if len(operands) > 1:
                left_part = self._evaluate(operands[0])
                right_part = self._evaluate(operands[1])
                return self.op_class[operator](left_part, right_part)

        return Number(float(expression_part))


    def evaluate(self) -> Add | Sub | Mul | Div | Pow | Number:
        return self._evaluate(self.expression)


ctx = Context("4+2/2+3")
expr = ctx.evaluate()
print(expr.interpret())

