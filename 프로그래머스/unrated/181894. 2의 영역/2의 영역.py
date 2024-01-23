def solution(arr):
    answer = []
    
    s=[]
    for i in range(len(arr)):
        if arr[i]==2:
            s.append(i)
            
    if len(s)==0:
        answer.append(-1)
    else:
        for i in range(s[0], s[-1]+1):
            answer.append(arr[i])
                
    return answer