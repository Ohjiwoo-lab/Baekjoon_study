def solution(prices):
    n=len(prices)
    answer = [0]*n
    
    stack=[]
    stack.append([0,prices[0]])
    
    time=1
    while stack and time<n:
        if stack[-1][1]<=prices[time]:
            stack.append([time,prices[time]])
            time+=1
        else:
            while stack:
                if stack[-1][1]>prices[time]:
                    idx,num=stack.pop()
                    answer[idx]=time-idx
                else:
                    break
            
            stack.append([time,prices[time]])
            time+=1
    
    while stack:
        idx,num=stack.pop()
        answer[idx]=time-1-idx
    
    return answer