""" 
1. Реализовать класс Context, который будет принимать обязательный аргумент expression
- это строка с математическим выражением. у класса также будет метод evaluate, в
котором нужно рекурсивно разобрать expression на составляющие и вернуть переформатированное 
выражение, где числа будут обернуты в [x], а операторы с операндами в (x*y):
ctx = Context("3*2 + 7^3")
print(ctx.evaluate())
# (([3] * [2]) + ([7] ^ [3]))
"""


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
        
    
    def _eval(self, substring: str) -> str:
        """ 
        The method parses the expression into a binary tree, then collects this tree to the top.
        
        :param substring: a string that can be a number or a mathematical expression 
        :returns: return wrapped substring by rules: number wrapped by [], expression wrapped by ().
        """
        substring = substring.strip()
        if substring.isdigit() or substring.replace('.', '', 1).isdigit():
            return f'[{substring}]'
        
        for op in self.op_order:
            if op not in substring:
                continue
            
            parts = substring.split(op, 1)
            return f'({self._eval(parts[0])} {op} {self._eval(parts[1])})'
        
    
    def evaluate(self) -> str:
        """ 
        :returns: return string where string wrapped by rules: number wrapped by [], all expression wrapped by (). 
        """
        return self._eval(self.expression)


ctx = Context("3*2 + 7^3")
print(ctx.evaluate())


ctx = Context("3.57657*2.436554 -1 + 7^3")
print(ctx.evaluate())