heights=list(map(int,input().split()))
def solution():
    stack=[]
    for i in range(len(heights)):
        start=i
        while stack and stack[-1][1]>heights[i]:
            index,height=stack.pop()
            max_area=max(max_area,height*(i-index))
            start=index
        stack.append((start,heighs[i]))
    n = len(heights)

    while stack:
        index, height = stack.pop()
        max_area = max(max_area, height * (n - index))

    return max_area

print(solution())
        
