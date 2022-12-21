""" 
2. Расширить функционал, добавив класс Number, с обязательным аргументом - value,
который будет представлять любое число в выражениях, а также классы Add(сумма),
Sub(разность), Mul(умножение), Div(деление), Pow(степень) - которые представляют
все возможные операции, и принимают два обязательных аргумента left - левый операнд,
right - правый операнд, операндом может быть любой объект выше перечисленных
классов. У всех упомянутых классов должен быть метод interpret(), который будет 
возвращать вычисленное значение типа float(к примеру "4".interpret() -> 4, "3*2".interpret()
-> 6). Все исключительные ситуации отловить try/except блоками. Также нужно изменить
реализацию метода Context.evaluate() так, чтобы он возвращал не строку, а объект
одного из выше указанных классов. Обязательно указывать аннотации и пользоваться
только описанными классами.
ctx = Context("3*2 + 7^3")
print(ctx.evaluate())
# 349
"""
from __future__ import annotations
from typing import Any
from sys import stdin


class Number(object):
    def __init__(self, value: str) -> None:
        """ 
        :param value: value is float or int
        """
        self.value = float(value) if '.' in value else int(value)
    
    
    def interpret(self) -> int | float:
        """ 
        :returns: return value (int or float)
        """
        return self.value


class Add(object):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() + self.right.interpret()


class Sub(object):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() - self.right.interpret()
    

class Mul(object):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() * self.right.interpret()


class Div(object):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() / self.right.interpret()


class Pow(object):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() ** self.right.interpret()
    
    
class Context(object):
    """
    :attribute op_order: list containing mathematical operators
    """
    op_order = ['+', '-', '*', '/', '^']
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
            return Number(substring)
        
        for op in self.op_order:
            if op not in substring:
                continue
            
            parts = substring.split(op, 1)
            if op == '+':
                return Add(self._eval(parts[0]), self._eval(parts[1]))
            elif op == '-':
                return Sub(self._eval(parts[0]), self._eval(parts[1]))
            elif op == '*':
                return Mul(self._eval(parts[0]), self._eval(parts[1]))
            elif op == '/':
                return Div(self._eval(parts[0]), self._eval(parts[1]))
            elif op == '^':
                return Pow(self._eval(parts[0]), self._eval(parts[1]))
        
    
    def evaluate(self) -> int | float:
        """ 
        :returns: return result of expression 
        """
        return self._eval(self.expression)


for line in stdin:
    if line.strip() == 'exit':
        break
    
    try:    
        print(Context(line).evaluate().interpret())
    except ZeroDivisionError:
        print('Нельзя делить на 0')
    except AttributeError:
        print('Проверьте выражение которое вы ввели.')