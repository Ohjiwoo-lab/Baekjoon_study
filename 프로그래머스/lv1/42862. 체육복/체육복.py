def solution(n, lost, reserve):
    answer = 0
    
    temp = reserve[:]
    for i in temp:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            continue
    
    reserve.sort()
    for i in reserve:
        if len(lost)==0:
            break            
        if i-1 in lost:
            lost.remove(i-1)
            continue
        if i+1 in lost:
            lost.remove(i+1)
            continue
            
    answer = n-len(lost)
    
    return answer