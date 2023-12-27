def solution(order):
    answer = 0
    
    stack=[]
    n, cnt = len(order), 0
    
    for i in range(1, n+1):
        if i == order[cnt]:
            answer += 1
            cnt += 1
        elif stack:
            while stack:
                if stack[-1] == order[cnt]:
                    stack.pop()
                    answer += 1
                    cnt += 1
                else:
                    break
            stack.append(i)
        else:
            stack.append(i)
            
    while stack:
        num = stack.pop()
        if num == order[cnt]:
            answer += 1
            cnt += 1
        else:
            break
            
    return answer