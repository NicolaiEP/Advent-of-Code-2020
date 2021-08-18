import re

# APPROACH 1 (NEW):

with open("day_18/day_18_input.txt") as f:
    lines = [re.findall(r"(\d+|[^ 0-9])", line) for line in f.read().splitlines()]


def shunting_yard(expr):
    """Convert an infix math expression to postfix."""
    output = []
    operator_stack = []
    for token in expr:
        if token.isnumeric():
            output.append(token)
        elif token in ("+", "*"):
            while operator_stack and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack[-1] != "(":
                assert operator_stack, "Mismatched parenthesis."
                output.append(operator_stack.pop())
            assert operator_stack[-1] == "("
            operator_stack.pop()

    while operator_stack:
        output.append(operator_stack.pop())

    return output


def calc_postfix(expr):
    """Calculate a math expression with postfix notation."""
    stack = []
    for token in expr:
        if token in ("+", "*"):
            first = stack.pop()
            second = stack.pop()
            if token == "+":
                stack.append(first.__add__(second))
            elif token == "*":
                stack.append(first.__mul__(second))
        elif token:
            stack.append(int(token))
    return stack.pop()


print(sum(calc_postfix(shunting_yard(line)) for line in lines))


# APPROACH 2 (OLD):
with open("day_18/day_18_input.txt") as f:
    lines = [re.sub(r"(\d+)", r"(\1)", line).replace(" + ", ".__add__").replace(" * ", ".__mul__")
             for line in f.read().splitlines()]

print(sum(eval(line) for line in lines))
