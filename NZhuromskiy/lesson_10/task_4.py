"""
4. Добавить реализацию поэтапного вывода операций.
5. Добавить искючение: делить на ноль запрещено.
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class CustomZeroDivision(Exception):
    """
    Класс пользовательского исключения для деления на ноль.
    """
    ...


class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self) -> float:
        """
        Абстрактный метод интерпретации математического выражения.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class TerminalExpression(AbstractExpression):
    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
        """
        Возвращает значение числа.

        :return: значение числа (float)
        """
        return self.value

    def __str__(self) -> str:
        return str(self.value)


class NonTerminalExpression(AbstractExpression):
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | TerminalExpression,
                 right: Add | Sub | Mul | Div | Pow | TerminalExpression,
                 ) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{str(self.left)} {str(self.right)}"


class Number(TerminalExpression):
    pass


class Add(NonTerminalExpression):
    def interpret(self) -> float:
        """
        Возвращает результат сложения двух выражений.

        :return: результат сложения (float)
        """
        return self.left.interpret() + self.right.interpret()

    def __str__(self) -> str:
        return f"({str(self.left)} + {str(self.right)})"


class Sub(NonTerminalExpression):
    def interpret(self) -> float:
        """
        Возвращает результат вычитания двух выражений.

        :return: результат вычитания (float)
        """
        return self.left.interpret() - self.right.interpret()

    def __str__(self) -> str:
        return f"({str(self.left)} - {str(self.right)})"


class Mul(NonTerminalExpression):
    def interpret(self) -> float:
        """
        Возвращает результат умножения двух выражений.

        :return: результат умножения (float)
        """
        return self.left.interpret() * self.right.interpret()

    def __str__(self) -> str:
        return f"({str(self.left)} * {str(self.right)})"


class Div(NonTerminalExpression):
    def interpret(self) -> float:
        """
        Возвращает результат деления двух выражений.

        :return: результат деления (float)
        :raises CustomZeroDivision: если происходит деление на ноль
        """
        try:
            return self.left.interpret() / self.right.interpret()
        except ZeroDivisionError:
            raise CustomZeroDivision

    def __str__(self) -> str:
        return f"({str(self.left)} / {str(self.right)})"


class Pow(NonTerminalExpression):
    def interpret(self) -> float:
        """
        Возвращает результат возведения одного выражения в степень другого.

        :return: результат возведения в степень (float)
        """
        return self.left.interpret() ** self.right.interpret()

    def __str__(self) -> str:
        return f"({str(self.left)} ^ {str(self.right)})"


class Context:
    # Словарь операторов и соответствующих им классов
    op_map: dict = {
        '+': Add,
        '-': Sub,
        '/': Div,
        '*': Mul,
        '^': Pow,
    }

    def __init__(self, expression: str) -> None:
        """
        Инициализация объекта контекста с заданным выражением.

        :param expression: строка, представляющая математическое выражение
        """
        self.expression = expression

    @staticmethod
    def _eval(expression: str) -> Add | Sub | Div | Mul | Pow | TerminalExpression:
        """
        Рекурсивная функция для создания объектов операторов и чисел, представляющих
        математическое выражение.

        :param expression: строка, представляющая математическое выражение
        :return: объект оператора или числа, представляющий выражение
        """
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

            current_node = Context.op_map[op](left, right)
            print(current_node)  # Вывод текущего уровня дерева
            return current_node

    def evaluate(self) -> Add | Sub | Div | Mul | Pow | TerminalExpression:
        """
        Создает дерево объектов операторов и чисел, представляющих
        математическое выражение объекта контекста.

        :return: корень дерева объектов операторов и чисел
        """
        return self._eval(self.expression)


try:
    ctx = Context('3*2 + 7^3')
    expr = ctx.evaluate()
    print("Результат:", expr.interpret())
except CustomZeroDivision:
    print("Ошибка: деление на ноль запрещено.")
