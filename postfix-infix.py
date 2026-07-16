exp = input()

def postfix_to_infix():
    stack = []

    for ch in exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append("(" + op1 + ch + op2 + ")")

    return stack[-1]

print(postfix_to_infix())
