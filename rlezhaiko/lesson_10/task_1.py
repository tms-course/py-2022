""" 
1. Написать калькулятор математических выражений на базе шаблона проектирования
Интерпретатор с возможностью вывода последовательности вычислений, все исключительные
ситуации отловить try/except блоками, чтобы не дать программе упасть. Поддерживаемые
операции: умножение, деление, сложениек, разность, степень. На ввод программе можно 
передавать выражения типа:
python calc.py
? 10 * 2 + 3 ** 2
= 10 * 2 + 9
= 20 + 9
= 29
? 2.34 ** 2 - 6 / 0
= 5.4756 - 6 / 0
= Нельзя делить на 0
"""
from sys import stdin


sequence_of_operations = ['**', '*', '/', '+', '-']


def check_elements(elements: list) -> list:
    """
    Check elements function
    Check first element and length elements for valid
    
    :param elements: list of element
    :returns: return list of element
    """
    if elements[0] == '?':
        elements.pop(0)
    else:
        raise IndexError
    
    if len(elements) < 3:
        raise IndexError
    
    return elements


def make_operation(operand_1: int | float, operator: str, operand_2: int | float) -> int | float:
    """
    Check elements function
    Check first element and length elements for valid
    
    :param operand_1: first operand
    :param operator: operator
    :param operand_2: second operand
    :returns: return result of operation
    """
    result = 0
    if operator == '**':
        result = operand_1 ** operand_2
    elif operator == '*':
        result = operand_1 * operand_2
    elif operator == '/':
        result = operand_1 / operand_2
    elif operator == '+':
        result = operand_1 + operand_2
    elif operator == '-':
        result = operand_1 - operand_2
    else:
        raise IndexError
    
    return result


for line in stdin:
    line = line.strip()
    if line == 'exit':
        break
    
    try:
        elements = line.split()
        elements = check_elements(elements)
        for operator in sequence_of_operations:
            operator_count = elements.count(operator)
            for i in range(operator_count):
                index_of_operator = elements.index(operator)
                index_of_operand_1, index_of_operand_2 = index_of_operator - 1, index_of_operator + 1
                operand_1 = float(elements[index_of_operand_1]) if '.' in elements[index_of_operand_1] else int(elements[index_of_operand_1])
                operand_2 = float(elements[index_of_operand_2]) if '.' in elements[index_of_operand_2] else int(elements[index_of_operand_2])
                result = make_operation(operand_1, elements[index_of_operator], operand_2)
                for i in range(index_of_operand_2, index_of_operand_1 - 1, -1):
                    elements.pop(i)
                elements.insert(index_of_operand_1, str(result))
                print('=', *elements)
    except IndexError:
        print('Проверьте строку которую Вы ввели!')
    except ZeroDivisionError:
        print('Нельзя делить на 0')
    except ValueError:
        print('Вы пытаетесь выполнить математическую операцию не с числом')