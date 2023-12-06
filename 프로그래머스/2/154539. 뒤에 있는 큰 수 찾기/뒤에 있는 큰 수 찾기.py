def solution(numbers):
    answer = [-1]*(len(numbers))
    
    num=[]
    for i, n in enumerate(numbers):
        num.append([i,n])
        
    stack=[]
    for i, n in num:
        while stack:
            if stack[-1][1] < n:
                cnt,_ = stack.pop()
                answer[cnt]=n
            else:
                break
        
        stack.append([i,n])
    
    return answer