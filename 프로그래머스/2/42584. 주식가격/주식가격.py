def solution(prices):
    answer = []
    
    n=len(prices)
    for i in range(n):
        flag=True
        cnt=1
        for j in range(i+1,n):
            if prices[i]<=prices[j]:
                cnt+=1
            else:
                answer.append(cnt)
                flag=False
                break
        
        if flag:
            answer.append(cnt-1)
    
    return answer