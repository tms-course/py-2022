"""Расширить функционал, добавив класс Number, с обязательным аргументом - value,
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
# 349"""

from __future__ import annotations

class CustomZeroDivsion(Exception):...


class Number:
    """:param value: value in float"""
    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
        """:returns: return value"""
        return self.value
    
class Add:
    def __init__(
            self, 
            left: 'Add' | Sub | Mul | Div | Pow | Number, 
            right: 'Add' | Sub | Mul | Div | Pow | Number
            ) -> None:
        """:param left: left part expression
           :param right: right part expression"""
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()

class Sub:
    def __init__(
            self, 
            left: 'Add' | Sub | Mul | Div | Pow | Number, 
            right: 'Add' | Sub | Mul | Div | Pow | Number
            ) -> None:
        """:param left: left part expression
           :param right: right part expression"""
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()


class Mul:
    def __init__(
            self, 
            left: 'Add' | Sub | Mul | Div | Pow | Number, 
            right: 'Add' | Sub | Mul | Div | Pow | Number
            ) -> None:
        """:param left: left part expression
           :param right: right part expression"""
        self.left = left
        self.right = right

    def interpret(self)->float:
        return self.left.interpret() * self.right.interpret()
    

class Div:
    def __init__(
            self, 
            left: 'Add' | Sub | Mul | Div | Pow | Number, 
            right: 'Add' | Sub | Mul | Div | Pow | Number
            ) -> None:
        """:param left: left part expression
           :param right: right part expression"""
        self.left = left
        self.right = right

    def interpret(self) -> float:
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            raise CustomZeroDivsion
        

class Pow:
    def __init__(
            self, 
            left: 'Add' | Sub | Mul | Div | Pow | Number, 
            right: 'Add' | Sub | Mul | Div | Pow | Number
            ) -> None:
        """:param left: left part expression
           :param right: right part expression"""
        self.left = left
        self.right = right

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
    def _eval(expression: str)-> Add | Sub | Div | Mul | Pow | Number:
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

        

    def evaluate(self)-> Add | Sub | Div | Mul | Pow | Number:
        """:return wrapped expression as a string"""
        return self._eval(self.expression)
    
ctx = Context("7/4 * 3^4")
expr = ctx.evaluate()
print(expr.interpret())