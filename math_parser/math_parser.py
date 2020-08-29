from math_parser.operators import *
import math


def simplify(expression: list) -> list:
    result = []
    tmp = ''
    for element in expression:
        if element in ('+', '-'):
            tmp += element
        else:
            if tmp != '' and (tmp.count('-') % 2) == 0:
                result.append('+')
            elif tmp != '' and (tmp.count('-') % 2) == 1:
                result.append('-')
            tmp = ''
            result.append(element)
    print(result)
    return result


def parse(expression: str) -> list:
    expression = expression.replace(' ', '').replace(',', '.').replace('—', '-') + '\\'  # backslash for end of string
    tmp_expression = []
    tmp_ch = ''
    for ch in expression:
        if ch.isdigit() or ch == '.':
            tmp_ch += ch
        else:
            if tmp_ch != '':
                tmp_expression.append(tmp_ch)
            tmp_expression.append(ch)
            tmp_ch = ''
    return tmp_expression[:-1]


def priority(op):
    first_operations = ('^', '**')
    second_operations = ('*', '/')
    third_operations = ('+', '-')
    return 0 if op in third_operations else \
        1 if op in second_operations else \
        2 if op in first_operations else -1


def polish_notation(expression):
    expression = simplify(parse(expression))
    print(expression)
    output, operations = [], []
    for element in expression:
        # print(output, operations, sep='\n', end='\n\n')
        if element[0].isdigit():
            output.append(element)
        elif element == '(':
            operations.append(element)
        elif element == ')':
            last_parenthesis_index = ''.join(operations).rindex('(')
            output.extend(operations[last_parenthesis_index + 1::][::-1])
            del operations[last_parenthesis_index::]
        elif priority(element) == -1:
            return
        elif len(operations) and operations[-1] != '(' and priority(element) <= priority(operations[-1]):
            output.append(operations.pop())
            operations.append(element)
        else:
            operations.append(element)
    output.extend(operations[::-1])
    # print(output)
    return output


def solve_expression(expression):
    if not polish_notation(expression):
        return "Ø"
    expression = polish_notation(expression)
    output = []
    # print(expression)
    for element in expression:
        if element[0].isdigit():
            output.append(float(element))
        else:
            try:
                output.append(operators[element](output.pop(-2), output.pop()))
            except ZeroDivisionError:
                return "Ø"
    answer = round(output.pop(), 8)
    return int(answer) if math.modf(answer)[0] == 0.0 else answer
