"""
+ Добавил последовательный вывод операций и Делить на ноль нельзя задание 4 и 5.

3. Ввести уровень абстракции в текущую реализацию добавив классы TerminalExpression с
обязательным аргументом value: float, представляющий значения, которые нельзя разбить на части - это числа, 
класс Number должен быть унаследован от этого класса,
NonTerminalExpression с двумя обязательными аргументами left - левый операнд, right
- правый операнд, который будет представлять любое комплексное выражение, т.е все
классы операций Add, ..., Pow должны быть унаследованы от этого класса. И последним мы добавим класс AbstractExpression, 
который будет представлять любое выражение в программе, и который будет иметь только один абстрактный метод(смотреть
@abc.abstractmethod) - interpret() возвращающий вычисленное значение float. Классы
TerminalExpression и NonTerminalExpression должны быть унаследованы от него.
"""


import abc


class AbstractExpression(abc.ABC):
    """
    Абстрактный класс AbstractExpression представляет любое выражение в программе.
    """

    @abc.abstractmethod
    def interpret(self) -> float:
        """
        Абстрактный метод interpret возвращает вычисленное значение выражения.

        :return: вычисленное значение выражения.
        """
        pass


class TerminalExpression(AbstractExpression):
    """
    Класс TerminalExpression представляет значения, которые нельзя разбить на части,
    такие как числа.
    """

    def __init__(self, value: float):
        """
        Инициализация объекта TerminalExpression с заданным значением.

        :param value: значение числа.
        """
        self.value = value

    def interpret(self) -> float:
        """
        Возвращает значение числа.

        :return: значение числа.
        """
        return self.value


class NonTerminalExpression(AbstractExpression):
    """
    Класс NonTerminalExpression представляет любое комплексное выражение,
    состоящее из левого и правого операндов.
    """

    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        """
        Инициализация объекта NonTerminalExpression с заданными левым и правым операндами.

        :param left: левый операнд.
        :param right: правый операнд.
        """
        self.left = left
        self.right = right


class Add(NonTerminalExpression):
    """
    Класс Add представляет операцию сложения.
    """

    def interpret(self) -> float:
        """
        Возвращает результат сложения левого и правого операндов.

        :return: результат сложения.
        """
        return self.left.interpret() + self.right.interpret()


class Sub(NonTerminalExpression):
    """
    Класс Sub представляет операцию вычитания.
    """

    def interpret(self) -> float:
        """
        Возвращает результат вычитания правого операнда из левого.

        :return: результат вычитания.
        """
        return self.left.interpret() - self.right.interpret()


class Mul(NonTerminalExpression):
    """
    Класс Mul представляет операцию умножения.
    """

    def interpret(self) -> float:
        """
        Возвращает результат умножения левого и правого операндов.

        :return: результат умножения.
        """
        return self.left.interpret() * self.right.interpret()


class Div(NonTerminalExpression):
    """
    Класс Div представляет операцию деления.
    """

    def interpret(self) -> float:
        """
        Возвращает результат деления левого операнда на правый.

        :return: результат деления.
        """
        right_value = self.right.interpret()
        if right_value == 0:
            raise ValueError("Делить на ноль нельзя")
        return self.left.interpret() / right_value


class Pow(NonTerminalExpression):
    """
    Класс Pow представляет операцию возведения в степень.
    """

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

    def process_expression(self, expression_part: str):
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
        return TerminalExpression(float(expression_part))

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


def evaluate_with_log(expression: str) -> float:
    """
    Функция evaluate_with_log вычисляет результат математического выражения
    и выводит его вместе с исходным выражением. В случае возникновения ошибки,
    выводится соответствующее сообщение об ошибке.

    :param expression: математическое выражение в виде строки.
    :return: результат вычисления выражения.
    """
    context = Context(expression)
    try:
        result = context.evaluate()
        print(f"{expression} = {result}")
        return result
    except ValueError as e:
        print(f"Ошибка: {e}")


ctx = Context("3*2 + 7^3")
print(ctx.evaluate())
evaluate_with_log("3*2 + 7^3")
evaluate_with_log("10 / 2")
evaluate_with_log("5 / 0")  # Делить на ноль нельзя
