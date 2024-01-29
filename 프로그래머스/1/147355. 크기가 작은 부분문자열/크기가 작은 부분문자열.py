def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):
        tmp = ''
        for j in range(i,i+len(p)):
            tmp += t[j]
        
        if int(p)>=int(tmp):
            answer += 1
    
    return answer