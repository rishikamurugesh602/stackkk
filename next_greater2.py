nums = list(map(int, input().split()))

def solution():
    n = len(nums)
    ans = [-1] * n
    stack = []   # stores indices

    for i in range(2 * n):
        index = i % n
        while stack and nums[index] > nums[stack[-1]]:
            ans[stack.pop()] = nums[index]
        if i < n:
            stack.append(index)

    return ans


print(solution())
