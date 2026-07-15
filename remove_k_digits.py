nums=input()
k=int(input())
def solution(nums,k):
    stack=[]
    for num in nums:
        while stack and stack[-1]>num and k>0:
            k-=1
            stack.pop()
        stack.append(num)
    if k>0:
        for _ in range(k):
            stack.pop()
    return "".join(stack)
                
        

print(solution(nums,k))
