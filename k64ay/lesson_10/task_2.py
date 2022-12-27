"""
Расширить функционал, добавив класс Number, у которого будет один обязательный аргумент - value, и который будет представлять любое число в выражениях,
а также классы Add(сумма), Sub(разность), Mul(умножение), Div(деление), Pow(степень) - которые представляют все возможные операции, и принимают два
обязательных аргумента left - левый операнд, right - правый операнд, операндом может быть любой объект выше перечисленных классов. 
У всех упомянутых классов должен быть метод interpret(), который будет возвращать вычисленное значение типа float(к примеру "4".interpret() -> 4, "3*2".interpret() -> 6). 
Также нужно изменить реализацию метода Context.evaluate() так, чтобы он возвращал не строку, а объект одного из выше указанных классов.
Обязательно указывать аннотации.
"""
from __future__ import annotations

line = "3*2 + 7^3 + 10 - 5/2"

class Number:
    def __init__(self, value: float):
        self.value = value

    def interpret(self) -> float:
        return self.value


class Add:
    def __init__(self, 
        left: Add | Sub | Mul | Div | Pow | Number, 
        right: Add | Sub | Mul | Div | Pow | Number
    ):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()


class Sub:
    def __init__(self, 
        left: Add | Sub | Mul | Div | Pow | Number, 
        right: Add | Sub | Mul | Div | Pow | Number
    ):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret() 
    

class Mul:
    def __init__(self, 
        left: Add | Sub | Mul | Div | Pow | Number, 
        right: Add | Sub | Mul | Div | Pow | Number
    ):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() * self.right.interpret() 


class Div:
    def __init__(self, 
        left: Add | Sub | Mul | Div | Pow | Number, 
        right: Add | Sub | Mul | Div | Pow | Number
    ):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() / self.right.interpret() 


class Pow:
    def __init__(self, 
        left: Add | Sub | Mul | Div | Pow | Number, 
        right: Add | Sub | Mul | Div | Pow | Number
    ):
        self.left = left
        self.right = right

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

    def __eval(self, expression: str) -> Add | Sub | Mul | Div | Pow | Number:
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

    def evaluate(self) -> Add | Sub | Mul | Div | Pow | Number:
        return self.__eval(self.expression)

ctx = Context()
ex = ctx.evaluate(line)
print(ex.interpret())

