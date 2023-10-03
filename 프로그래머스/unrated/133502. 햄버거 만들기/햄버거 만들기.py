def solution(ingredient):
    answer = 0

    stack=[]
    for i in ingredient:
        n=len(stack)
        if n>=3 and i==1:
            if stack[n-1]==3:
                if stack[n-2]==2:
                    if stack[n-3]==1:
                        for j in range(3):
                            stack.pop()
                        answer+=1
                        continue
        stack.append(i)
    
    return answer