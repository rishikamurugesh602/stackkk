nums = list(map(int, input().split()))

def solution():
    n = len(nums)
    ans=[-1]*n
    stack=[]
    for i in range(n):
        while stack and nums[stack[-1]]<nums[i]:
            stack.pop()
        if stack:
            ans[i]=nums[stack[-1]]
        stack.append(i)
    return ans

print(solution())
