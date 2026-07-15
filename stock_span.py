nums = list(map(int, input().split()))

def solution():
    n = len(nums)
    ans=[1]*n
    stack=[]
    count=0
    for i in range(n):
        while stack and nums[stack[-1]]<=nums[i]:
            stack.pop()
        if stack:
            ans[i]=i-stack[-1]
        else:
            ans[i]=i+1
        stack.append(i)
    return ans

print(solution())
