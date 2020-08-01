def parse_expression(expression):
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
    first_operations = {'*', '/', '(', ')'}
    second_operations = {'+', '-'}
    return 0 if operator in first_operations else \
           1 if operator in second_operations else -1


def solve_expression(expression):
    expression = parse_expression(expression)
    output, operations = [], []
    for element in expression:
        if element[0].isdigit():
            output.append(element)
        else:
            operations.append(element)

    print(output)
    print(operations)
    return


solve_expression("234 +   2")
