nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
def solution():
    nge={}
    stack=[]
    for num in nums2:
        while stack and num>stack[-1]:
            nge[stack.pop()]=num
        stack.append(num)
    while stack:
        nge[stack.pop()]=-1
    return [nge[num] for num in nums1]
ans=solution()
print(ans)
