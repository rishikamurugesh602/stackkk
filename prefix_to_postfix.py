exp = input()

def prefix_to_postfix():
    stack = []

    for ch in reversed(exp):
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + ch)

    return stack[-1]

print(prefix_to_postfix())
