def solution(s):
    answer = True
    
    stack=[]
    for i in s:
        if len(stack)==0 and i==")":
            answer=False
            break
        elif i=="(":
            stack.append(i)
        else:
            if stack[len(stack)-1]=="(":
                stack.pop()
            else:
                stack.append(i)
    
    if len(stack)!=0:
        answer=False

    return answer