nums = list(map(int, input().split()))

def solution():
    n = len(nums)
    ans=[0]*n
    stack=[]
    count=0
    for i in range(n):
        while stack and nums[stack[-1]]<nums[i]:
            index=stack.pop()
            count=i-index
            ans[index]=count
        stack.append(i)
    return ans
            
    
            


print(solution())
