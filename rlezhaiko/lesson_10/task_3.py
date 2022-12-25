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
from sys import stdin
from abc import abstractmethod
from string import punctuation


class AbstractExpression(object):
    """ 
    All Terminal and Non-Terminal expressions will implement an interpret method
    """
    @abstractmethod
    def interpret(self):
        raise NotImplementedError


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
    def __init__(self, left: AbstractExpression, right: AbstractExpression) -> None:
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
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            raise CustomZeroDivisionError('Нельзя делить на 0')


class Pow(NonTerminalExpression):
    def interpret(self) -> float:
        return self.left.interpret() ** self.right.interpret()
    
    
class Context(object):
    """
    :attribute op_map: dict containing key: mathematical operator, value: class represent mathematical operator 
    """
    op_map = {'+': Add, 
              '-': Sub, 
              '*': Mul, 
              '/': Div,
              '^': Pow}
    def __init__(self, expression: str) -> None:
        """ 
        :param expression: expression from user input 
        """
        self.expression = expression


    def _eval(self, substring: str) -> AbstractExpression:
        """ 
        The method parses the expression into a binary tree, then collects this tree to the top.
        
        :param substring: a string that can be a number or a mathematical expression 
        :returns: return the class represented by a mathematical operation or a number
        """
        substring = substring.strip()
        if substring.isdigit() or substring.replace('.', '', 1).isdigit():
            return Number(float(substring))
        elif substring == '' or substring.isalpha() or substring in punctuation:
            raise IncorrectExpressionError('Введенно неверное математическое выражение.')
        
        for op in Context.op_map:
            if op not in substring:
                continue
            
            parts = substring.split(op, 1)
            left = self._eval(parts[0])
            right = self._eval(parts[1])
            return self.op_map[op](left, right)
        
    
    def evaluate(self) -> float:
        """ 
        :returns: return result of expression 
        """
        return self._eval(self.expression)


class CustomZeroDivisionError(Exception):
    pass


class IncorrectExpressionError(Exception):
    pass


for line in stdin:
    if line.strip() == 'exit':
        break
    
    try:    
        print(Context(line).evaluate().interpret())
    except CustomZeroDivisionError as error:
        print(error)
    except IncorrectExpressionError as error:
        print(error)
    except AttributeError:
        print('Проверьте выражение которое вы ввели.')