from heapq import heappush, heappop
from collections import deque

def solution(priorities, location):
    answer = 0
    
    process=deque()
    q=[]
    for i, num in enumerate(priorities):
        process.append([i,num])
        heappush(q, -num)
    
    cnt=0
    while process:
        i, num = process.popleft()
        if num==(-q[0]):
            cnt+=1
            if i==location:
                answer=cnt
                break
            else:
                heappop(q)
        else:
            process.append([i,num])
    
    return answer