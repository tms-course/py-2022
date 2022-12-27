from task_3 import TerminalExpression, NonTerminalExpression


class Number(TerminalExpression):
    def interpret(self):
        return self.value


class Add(NonTerminalExpression):
    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Sub(NonTerminalExpression):

    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class Mul(NonTerminalExpression):
    def interpret(self):
        return self.left.interpret() * self.right.interpret()


class Div(NonTerminalExpression):

    def interpret(self):
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            print('Division by zero error')
            raise SystemExit


class Pow(NonTerminalExpression):

    def interpret(self):
        return self.left.interpret() ** self.right.interpret()
