from __future__ import annotations
from typing import Any
from sys import stdin
from abc import abstractmethod


class AbstractExpression(object):
    """ 
    All Terminal and Non-Terminal expressions will implement an interpret method
    """
    @abstractmethod
    def interpret(self):
        pass

    def __str__(self) -> str:
        pass

class TerminalExpression(AbstractExpression):
    """ 
    All Terminal expressions must be inherited from this class
    """
    def __init__(self, value: float) -> None:
        self.value = value
    
    
    def interpret(self) -> float:
        return self.value

    def __str__(self) -> str:
        return str(self.value)


class NonTerminalExpression(AbstractExpression):
    """ 
    All Non-Terminal expressions must be inherited from this class
    """
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    
    
    def interpret(self) -> float:
        pass


class Number(TerminalExpression):    
    def interpret(self) -> float:
        """ 
        :returns: return value (int or float)
        """
        return self.value


class Add(NonTerminalExpression):    
    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()
    
    def __str__(self) -> str:
        return f"{self.left} + {self.right}"


class Sub(NonTerminalExpression):    
    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()
    
    def __str__(self) -> str:
        return f"{self.left} - {self.right}"
    

class Mul(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() * self.right.interpret()
    
    def __str__(self) -> str:
        return f"{self.left} * {self.right}"


class Div(NonTerminalExpression):    
    def interpret(self) -> float:
        return self.left.interpret() / self.right.interpret()

    def __str__(self) -> str:
        return f"{self.left} / {self.right}"


class Pow(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() ** self.right.interpret()
    
    def __str__(self) -> str:
        return f"{self.left} ^ {self.right}"
    
    
class Context(object):
    """
    :attribute op_order: list containing mathematical operators
    """
    op_map = {
        '+': Add, 
        '-': Sub, 
        '*': Mul, 
        '/': Div, 
        '^': Pow
    }
    def __init__(self, expression: str) -> None:
        """ 
        :param expression: expression from user input 
        """
        self.expression = expression
        
    
    def _eval(self, substring: str) -> Any:
        """ 
        The method parses the expression into a binary tree, then collects this tree to the top.
        
        :param substring: a string that can be a number or a mathematical expression 
        :returns: return the class represented by a mathematical operation or a number
        """
        substring = substring.strip()
        if substring.isdigit() or substring.replace('.', '', 1).isdigit():
            value = float(substring)
            return Number(value)
        
        for op in self.op_map:
            if op not in substring:
                continue
            
            lsub, rsub = substring.split(op, 1)
            left = self._eval(lsub)
            right = self._eval(rsub)

            return self.op_map[op](left, right)
        
    
    def evaluate(self) -> int | float:
        """ 
        :returns: return result of expression 
        """
        return self._eval(self.expression)


class OrderIterator:
    def __init__(self, expr: AbstractExpression):
        self.exrp = expr

    def __iter__(self) -> AbstractExpression:
        self.current_state = self.exrp

        return self

    @staticmethod
    def _fold_up(state: NonTerminalExpression) -> AbstractExpression:

        if issubclass(state.left.__class__, NonTerminalExpression):
            state.left = OrderIterator._fold_up(state.left)
            return state

        if issubclass(state.right.__class__, NonTerminalExpression):
            state.right = OrderIterator._fold_up(state.right)
            return state

        return Number(state.interpret())

    def __next__(self) -> AbstractExpression:
        if issubclass(self.current_state.__class__, TerminalExpression):
            raise StopIteration

        self.current_state = self._fold_up(self.current_state)

        return self.current_state


for line in stdin:
    if line.strip() == 'exit':
        break
    
    try:
        ctx = Context(line)
        root_expr = ctx.evaluate()
        order_iterator = OrderIterator(root_expr)
        for expr in order_iterator:
            print(expr)
        
    except ZeroDivisionError:
        print('Нельзя делить на 0')
    except AttributeError:
        print('Проверьте выражение которое вы ввели.')