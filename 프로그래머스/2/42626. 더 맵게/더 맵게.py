from heapq import heappush, heappop

def solution(scoville, K):
    answer = -1
    
    q = []
    for i in scoville:
        heappush(q, i)
    
    cnt = 0
    while len(q)>1:
        if q[0] >= K:
            break
        
        n1 = heappop(q)
        n2 = heappop(q)
        heappush(q, n1+n2*2)
        
        cnt += 1
        
    if q[0] >= K:
        answer = cnt
    
    return answer