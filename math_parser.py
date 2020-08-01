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


def solve_expression(expression):
    expression = parse_expression(expression)
    first_operations = {'*', '/', '(', ')'}
    second_operations = {'+', '-'}
    output, operations = [], []
    print(expression)
    return


solve_expression("234 +   2")
