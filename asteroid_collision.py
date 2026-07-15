nums = list(map(int, input().split()))

def solution():
    stack = []
    for num in nums:
        alive = True
        while stack and stack[-1] > 0 and num < 0:
            if abs(stack[-1]) < abs(num):
                stack.pop()
            elif abs(stack[-1]) > abs(num):
                alive = False
                break
            else:
                stack.pop()
                alive = False
                break

        if alive:
            stack.append(num)

    return stack

print(solution())
