def solution(number, k):
    answer = ''
    
    stack=[]
    cnt=0
    for num in number:
        if cnt<k:
            while stack:
                if stack[-1] < num:
                    if cnt>=k:
                        break
                    stack.pop()
                    cnt+=1
                else:
                    break
            stack.append(num)
        
        else:
            stack.append(num)
    
    for i in range(k-cnt):
        stack.pop()
    
    for i in stack:
        answer+=i
    
    return answer