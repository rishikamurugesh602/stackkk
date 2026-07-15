nums = input().split()

def solution(nums):
    stack = []
    for token in nums:
        if token in "*+/-":
            num1 = stack.pop()
            num2 = stack.pop()

            if token == "+":
                result = num1 + num2
            elif token == "-":
                result = num2 - num1
            elif token == "*":
                result = num1 * num2
            else:
                result = int(num2 / num1)

            stack.append(result)
        else:
            stack.append(int(token))

    return stack[-1]

print(solution(nums))
