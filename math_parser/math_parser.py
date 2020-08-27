from math_parser.operators import *
import math


def parse_expression(expression: str) -> list:
    expression = expression.replace(' ', '') + '\\'  # backslash is added to know the end of string
    tmp_expression = []
    tmp_ch = ''
    for ch in expression:
        if ch.isdigit() or ch == '.':
            tmp_ch += ch
        elif ch == ',':
            tmp_ch += '.'
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
    expression = parse_expression(expression)
    output, operations = [], []
    for element in expression:
        # print(output, operations, sep='\n', end='\n\n')
        if element[0].isdigit():
            output.append(element)
        elif element == '(':
            operations.append(element)
        elif element == ')':
            last_parenthesis_index = ''.join(operations).rindex('(')
            output.extend(operations[last_parenthesis_index+1::][::-1])
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
