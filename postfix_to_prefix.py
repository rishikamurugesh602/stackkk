exp = input()

def postfix_to_prefix():
    stack = []

    for ch in exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(ch + op1 + op2)

    return stack[-1]

print(postfix_to_prefix())
