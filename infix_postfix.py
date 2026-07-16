exp = input()

def precedence(ch):
    if ch == "^":
        return 3
    elif ch in "*/":
        return 2
    elif ch in "+-":
        return 1
    return 0

def solution():
    result = []
    stack = []

    for ch in exp:
        if ch.isalnum():
            result.append(ch)

        elif ch == "(":
            stack.append(ch)

        elif ch == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()      # Remove '('

        else:  # Operator
            while (stack and stack[-1] != "(" and
                   (precedence(stack[-1]) > precedence(ch) or
                    (precedence(stack[-1]) == precedence(ch) and ch != "^"))):
                result.append(stack.pop())

            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return "".join(result)

print(solution())
