import task_3 as t3


class Number(t3.TerminalExpression):
    def __float__(self):
        return float(self.value)


class Add(t3.NonTerminalExpression):
    def interpret(self):
        return Number()


class Sub(t3.NonTerminalExpression):

    def interpret(self):
        return float(self.left) - float(self.right)


class Mul(t3.NonTerminalExpression):


    def interpret(self):
        return float(self.left) * float(self.right)


class Div(t3.NonTerminalExpression):

    def interpret(self):
        try:
            result = float(self.left) / float(self.right)
            return result
        except ZeroDivisionError:
            print('Division by zero error')
            raise SystemExit

class Pow(t3.NonTerminalExpression):

    def interpret(self):
        return float(self.left) ** float(self.right)
