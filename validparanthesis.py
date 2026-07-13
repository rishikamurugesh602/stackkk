string=input()
def solution():
    stack=[]
    for i in range(len(string)):
        if string[i] in "([{":
            stack.append(string[i])
        elif stack[-1]=="{" and string[i]=="}":
            stack.pop()
        elif stack[-1]=="(" and string[i]==")":
            stack.pop()
        elif stack[-1]=="[" and string[i]=="]":
            stack.pop()
        else:
            stack.append(string[i])
    if len(stack)==0:
        return True
    else:
        return False
        

ans=solution()
print(ans)
