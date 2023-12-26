def solution(plans):
    answer = []
    
    plans.sort(key=lambda x:x[1])

    stack=[]
    for name, time, minutes in plans:
        t = int(time.split(":")[0])*60 + int(time.split(":")[1])
        
        if stack:
            between = abs(stack[-1][0]-t)
            if between < stack[-1][1]:
                n, b, nm = stack.pop()
                stack.append([n+abs(n-t), b-abs(n-t), nm])
            else:
                while stack:
                    if between >= stack[-1][1]:
                        _, b, s = stack.pop()
                        answer.append(s)
                        between -= b
                    elif between > 0:
                        n, b, nm = stack.pop()
                        stack.append([n+between, b-between, nm])
                        break
                    else:
                        break
            stack.append([t, int(minutes), name])
        
        else:
            stack.append([t, int(minutes), name])
        
    while stack:
        _, _, s = stack.pop()
        answer.append(s)
    
    return answer