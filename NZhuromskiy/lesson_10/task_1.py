"""
1. Реализовать класс Context, который будет принимать обязательный аргумент expression
- это строка с математическим выражением. У класса также будет метод evaluate, в
котором нужно рекурсивно разобрать expression на составляющие и вернуть переформатированное выражение, 
где числа будут обернуты в [x], а операторы с операндами в (x*y).
"""


class Context:
    # Список поддерживаемых математических операторов
    op_map: list = ['+', '-', '/', '*', '^']

    def __init__(self, expression: str) -> None:
        """
        Инициализация объекта контекста с заданным выражением.

        :param expression: строка, представляющая математическое выражение
        """
        self.expression = expression

    @staticmethod
    def _eval(expression: str) -> str:
        """
        Вычисляет переданное математическое выражение и возвращает его
        в виде строки с расставленными скобками.

        :param expression: строка, представляющая математическое выражение
        :return: строка с выражением и расставленными скобками
        """
        prepared_expr = expression.strip()

        try:
            float(prepared_expr)
            return f'[{prepared_expr}]'
        except:
            pass

        for op in Context.op_map:

            if op not in prepared_expr:
                continue

            left_part, right_part = prepared_expr.split(op, 1)

            return f'({Context._eval(left_part)} {op} {Context._eval(right_part)})'

    def evaluate(self) -> str:
        """
        Вычисляет текущее выражение объекта контекста и возвращает его
        в виде строки с расставленными скобками.

        :return: строка с выражением и расставленными скобками
        """
        return self._eval(self.expression)


ctx = Context('3*2 + 7^3')
print(ctx.evaluate())
