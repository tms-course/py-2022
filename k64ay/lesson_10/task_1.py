cmd_line = "3*4 + 6^4"

class Context:
    op_order = ['+', '-', '*', '/', '^']
    def __init__(self, line: str) -> None:
        self.line = line

    def __eval(self, sub: str) -> str:
        sub = sub.strip()
        if sub.isdigit():
            return f'[{sub}]'

        for op in self.op_order:
            if op not in sub:
                continue

            parts = sub.split(op, 1)

            return f'({self.__eval(parts[0])} {op} {self.__eval(parts[1])})'
    

    def evaluate(self) -> str:
        return self.__eval(self.line)

ctx = Context(cmd_line)
print(ctx.evaluate())