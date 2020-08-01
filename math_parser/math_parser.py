import operators

def parse_expression(expression: str) -> list:
    expression = expression.replace(' ', '') + '\\'  # backslash is added to know the end of string
    tmp_expression = []
    tmp_ch = ''
    for ch in expression:
        if ch.isdigit():
            tmp_ch += ch
        else:
            tmp_expression.append(tmp_ch)
            tmp_expression.append(ch)
            tmp_ch = ''
    return tmp_expression[:-1]


def priority(operator):
    first_operations = {'*', '/'}
    second_operations = {'+', '-'}
    return 1 if operator in first_operations else \
        0 if operator in second_operations else -1


def polish_notation(expression):
    expression = parse_expression(expression)
    output, operations = [], []
    for element in expression:
        if element[0].isdigit():
            output.append(element)
        else:
            if priority(element) == -1:
                assert ValueError
            elif len(operations) and priority(element) <= priority(operations[-1]):
                output.append(operations.pop())
                operations.append(element)
            else:
                operations.append(element)
    output.extend(operations[::-1])
    return output

#
# def solve_expression(expression):
#     expression = polish_notation(expression)
#     print(expression)
#     output = []
#     for element in expression:
#         print(output)
#         if element[0].isdigit():
#             output.append(int(element))
#         else:
#             output.append(operators.operators[element](output.pop(), output.pop()))
#     return output
#
exp = "2 + 3  * 4"
print(exp)
print(polish_notation(exp))