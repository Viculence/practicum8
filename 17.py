def evaluate_expression(expr):
    operands = []
    operator_stack = []


    def apply_operator(operator):
        b = operands.pop()
        a = operands.pop()
        if operator == '+':
            operands.append(a + b)
        elif operator == '-':
            operands.append(a - b)
        elif operator == '*':
            operands.append(a * b)
        elif operator == '/':
            operands.append(a / b)

    operators = {'+', '-', '*', '/'}

    i = 0
    while i < len(expr):
        char = expr[i]

        if char.isdigit():
            number = 0
            while i < len(expr) and expr[i].isdigit():
                number = number * 10 + int(expr[i])
                i += 1
            operands.append(number)
            continue
        elif char in operators:
            while (operator_stack and operator_stack[-1] in operators and
                   char in ('+', '-') and operator_stack[-1] in ('*', '/')):
                apply_operator(operator_stack.pop())
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack[-1] != '(':
                apply_operator(operator_stack.pop())
            operator_stack.pop()
        i += 1

    while operator_stack:
        apply_operator(operator_stack.pop())

    return operands[0]


def main():
    expression = input("Введите выражение: ")
    print("Результат:", evaluate_expression(expression))

main()