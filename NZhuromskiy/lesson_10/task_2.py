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


class Number:
    """
    Класс Number представляет число в математическом выражении.
    """

    def __init__(self, value: float):
        """
        Инициализация объекта Number с заданным значением.

        :param value: значение числа.
        """
        self.value = value

    def interpret(self) -> float:
        """
        Возвращает значение числа.

        :return: значение числа.
        """
        return self.value


class Add:
    """
    Класс Add представляет операцию сложения.
    """

    def __init__(self, left: 'Expression', right: 'Expression'):
        """
        Инициализация объекта Add с заданными левым и правым операндами.

        :param left: левый операнд.
        :param right: правый операнд.
        """
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат сложения левого и правого операндов.

        :return: результат сложения.
        """
        return self.left.interpret() + self.right.interpret()


class Sub:
    """
    Класс Sub представляет операцию вычитания.
    """

    def __init__(self, left: 'Expression', right: 'Expression'):
        """
        Инициализация объекта Sub с заданными левым и правым операндами.

        :param left: левый операнд.
        :param right: правый операнд.
        """
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат вычитания правого операнда из левого.

        :return: результат вычитания.
        """
        return self.left.interpret() - self.right.interpret()


class Mul:
    """
    Класс Mul представляет операцию умножения.
    """

    def __init__(self, left: 'Expression', right: 'Expression'):
        """
        Инициализация объекта Mul с заданными левым и правым операндами.

        :param left: левый операнд.
        :param right: правый операнд.
        """
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат умножения левого и правого операндов.

        :return: результат умножения.
        """
        return self.left.interpret() * self.right.interpret()


class Div:
    """
    Класс Div представляет операцию деления.
    """

    def __init__(self, left: 'Expression', right: 'Expression'):
        """
        Инициализация объекта Div с заданными левым и правым операндами.

        :param left: левый операнд.
        :param right: правый операнд.
        """
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат деления левого операнда на правый.

        :return: результат деления.
        """
        return self.left.interpret() / self.right.interpret()


class Pow:
    """
    Класс Pow представляет операцию возведения в степень.
    """

    def __init__(self, left: 'Expression', right: 'Expression'):
        """
        Инициализация объекта Pow с заданными левым и правым операндами.

        :param left: левый операнд.
        :param right: правый операнд.
        """
        self.left = left
        self.right = right

    def interpret(self) -> float:
        """
        Возвращает результат возведения левого операнда в степень правого операнда.

        :return: результат возведения в степень.
        """
        return self.left.interpret() ** self.right.interpret()


class Context:
    """
    Класс Context предназначен для обработки и вычисления математических выражений.
    """

    OPERATORS = {
        '+': Add,
        '-': Sub,
        '*': Mul,
        '/': Div,
        '^': Pow
    }

    def __init__(self, expression: str):
        """
        Инициализация контекста с заданным выражением.

        :param expression: строка, содержащая математическое выражение для вычисления.
        """
        self.expression = expression

    @staticmethod
    def validate_expression(expression) -> bool:
        """
        Валидация математического выражения.

        :param expression: строка, содержащая математическое выражение для проверки.
        :return: True, если выражение валидно, иначе False.
        """
        for char in expression:
            if char not in Context.OPERATORS and not char.isdigit() and char != ' ':
                return False
        return True

    def process_expression(self, expression_part: str) -> 'Expression':
        """
        Рекурсивная обработка частей математического выражения.

        :param expression_part: строка, содержащая часть математического выражения для обработки.
        :return: объект одного из классов операций или класса Number.
        """
        expression_part = expression_part.strip()
        for operator, operator_class in self.OPERATORS.items():
            operands = expression_part.split(operator, 1)
            if len(operands) > 1:
                left_operand = self.process_expression(operands[0])
                right_operand = self.process_expression(operands[1])
                return operator_class(left_operand, right_operand)
        return Number(float(expression_part))

    def evaluate(self) -> float:
        """
        Вычисление математического выражения.

        :return: результат вычисления математического выражения.
        :raises ValueError: если выражение невалидно.
        """
        if not self.validate_expression(self.expression):
            raise ValueError('Expression is not valid')
        else:
            try:
                result = self.process_expression(self.expression)
                return result.interpret()
            except Exception as e:
                raise ValueError(f'Error during evaluation: {str(e)}')


ctx = Context("3*2 + 7^3")
print(ctx.evaluate())
