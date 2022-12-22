""" 
3. Ввести уровень абстракции в текущую реализацию добавив классы TerminalExpression с
обязательным аргументом value: float, представляющий значения, которые нельзя разбить
на части - это числа, класс Number должен быть унаследован от этого класса,
NonTerminalExpression с двумя обязательными аргументами left - левый операнд, right
- правый операнд, который будет представлять любое комплексное выражение, т.е. все
классы операций Add, ..., Pow должны быть унаследованы от этого класса. И последним
мы добавим класс AbstractExpression, который будет представлять любое выражение в программе,
и который будет иметь только один абстрактный метод(смотреть @abc.abstractmethod) - interpret()
возвращающий вычисленное значение float. Классы TerminalExpression и NonTerminalExpression 
должны быть унаследованы от него.
"""
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


class TerminalExpression(AbstractExpression):
    """ 
    All Terminal expressions must be inherited from this class
    """
    def __init__(self, value: float) -> None:
        """ 
        :param value: number in float format
        """
        self.value = value
    
    
    def interpret(self) -> float:
        """ 
        :returns: return value in float format
        """
        return self.value


class NonTerminalExpression(AbstractExpression):
    """ 
    All Non-Terminal expressions must be inherited from this class
    """
    def __init__(self, left: NonTerminalExpression | float, right: NonTerminalExpression | float) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self):
        pass


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
    
    
class Context(object):
    def __init__(self, expression: str) -> None:
        """ 
        :param expression: expression from user input 
        """
        self.expression = expression
        add = lambda left, right: Add(self._eval(left), self._eval(right))
        sub = lambda left, right: Sub(self._eval(left), self._eval(right))
        mul = lambda left, right: Mul(self._eval(left), self._eval(right))
        div = lambda left, right: Div(self._eval(left), self._eval(right))
        power = lambda left, right: Pow(self._eval(left), self._eval(right))
        self.op_map = {'+': add, 
                       '-': sub, 
                       '*': mul, 
                       '/': div,
                       '^': power}


    def _eval(self, substring: str) -> float | Add | Sub | Mul | Div | Pow:
        """ 
        The method parses the expression into a binary tree, then collects this tree to the top.
        
        :param substring: a string that can be a number or a mathematical expression 
        :returns: return the class represented by a mathematical operation or a number
        """
        substring = substring.strip()
        if substring.isdigit() or substring.replace('.', '', 1).isdigit():
            return Number(float(substring))
        
        for op in list(self.op_map.keys()):
            if op not in substring:
                continue
            
            parts = substring.split(op, 1)
            return self.op_map[op](parts[0], parts[1])
        
    
    def evaluate(self) -> float:
        """ 
        :returns: return result of expression 
        """
        return self._eval(self.expression)


class CustomZeroDivisionError(Exception):
    pass


for line in stdin:
    if line.strip() == 'exit':
        break
    
    try:    
        print(Context(line).evaluate().interpret())
    except CustomZeroDivisionError as error:
        print(error)
    except AttributeError:
        print('Проверьте выражение которое вы ввели.')