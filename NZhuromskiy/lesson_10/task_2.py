"""
2. Расширить функционал, добавив класс Number, с обязательным аргументом - value,
который будет представлять любое число в выражениях, а также классы Add(сумма),
Sub(разность), Mul(умножение), Div(деление), Pow(степень) - которые представляют
все возможные операции, и принимают два обязательных аргумента left - левый операнд, 
right - правый операнд, операндом может быть любой объект выше перечисленных
классов. У всех упомянутых классов должен быть метод interpret(), 
который будет возвращать вычисленное значение типа float(к примеру "4".interpret() -> 4, "3*2".interpret() -> 6). 
Все исключительные ситуации отловить try/except блоками. Также нужно изменить реализацию метода Context.evaluate() так, 
чтобы он возвращал не строку, а объект одного из выше указанных классов. Обязательно указывать аннотации и пользоваться
только описанными классами.
"""


from __future__ import annotations


class CustomZeroDivision(Exception):
    """
    Класс пользовательского исключения для деления на ноль.
    """
    ...


class Number:
    def __init__(self, value: float) -> None:
        self.value = value

    def interpret(self) -> float:
        """
        Возвращает значение числа.

        :return: значение числа (float)
        """
        return self.value


class Add:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number,
                 ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат сложения двух выражений.

        :return: результат сложения (float)
        """
        return self.left.interpret() + self.right.interpret()


class Sub:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number,
                 ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат вычитания двух выражений.

        :return: результат вычитания (float)
        """
        return self.left.interpret() - self.right.interpret()


class Mul:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number,
                 ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат умножения двух выражений.

        :return: результат умножения (float)
        """
        return self.left.interpret() * self.right.interpret()


class Div:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number,
                 ) -> None:
        self.left = left
        self.right = right

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


class Pow:
    def __init__(self,
                 left: Add | Sub | Mul | Div | Pow | Number,
                 right: Add | Sub | Mul | Div | Pow | Number,
                 ) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат возведения одного выражения в степень другого.

        :return: результат возведения в степень (float)
        """
        return self.left.interpret() ** self.right.interpret()


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
    def _eval(expression: str) -> Add | Sub | Div | Mul | Pow | Number:
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

            return Context.op_map[op](left, right)

    def evaluate(self) -> Add | Sub | Div | Mul | Pow | Number:
        """
        Создает дерево объектов операторов и чисел, представляющих
        математическое выражение объекта контекста.

        :return: корень дерева объектов операторов и чисел
        """
        return self._eval(self.expression)


ctx = Context('3*2 + 7^3')
expr = ctx.evaluate()
print(expr.interpret())
