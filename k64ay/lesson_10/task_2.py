from __future__ import annotations

class CustomZeroDivision(Exception): ...


class Number:
    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
        return self.value


class Add:
    def __init__(
            self, 
            left: 'Add' | Sub | Mul | Div | Pow | Number, 
            right: 'Add' | Sub | Mul | Div | Pow | Number
    ) -> None:
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
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() * self.right.interpret()
    

class Div:
    def __init__(
            self, 
            left: 'Add' | Sub | Mul | Div | Pow | Number, 
            right: 'Add' | Sub | Mul | Div | Pow | Number
    ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            raise CustomZeroDivision
    

class Pow:
    def __init__(
            self, 
            left: 'Add' | Sub | Mul | Div | Pow | Number, 
            right: 'Add' | Sub | Mul | Div | Pow | Number
    ) -> None:
        self.left = left
        self.right = right

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
    def _eval(expression: str) -> Add | Sub | Div | Mul | Pow | Number:
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


    def evaluate(self) -> Add | Sub | Div | Mul | Pow | Number:
        return self._eval(self.expression)
    
ctx = Context('3*2 + 7^3')
expr = ctx.evaluate()
print(expr.interpret())