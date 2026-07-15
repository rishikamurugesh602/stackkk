nums = list(map(int, input().split()))

def solution():
    n = len(nums)
    ans=[-1]*n
    stack=[]
    for i in range(n):
        while stack and nums[i]<=nums[stack[-1]]:
            index=stack.pop()
            ans[index]=nums[i]
        stack.append(i)
    return ans


print(solution())
