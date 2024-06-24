def solution(n):
    answer = 0
    
    a = []
    for i in str(n):
        a.append(int(i))
    
    a.sort()
    
    lenth = len(a)
    for i in range(lenth):
        answer += a[i]*(10**i)
    
    return answer