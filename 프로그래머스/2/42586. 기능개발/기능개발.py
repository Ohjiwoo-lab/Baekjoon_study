from heapq import heappush
from math import ceil

def solution(progresses, speeds):
    answer = []
    
    time,q = {},[]
    n=len(progresses)
    
    for i in range(n):
        t=ceil((100-progresses[i])/speeds[i])
        
        if q:
            if -q[0]>=t:
                time[-q[0]]+=1
            else:
                heappush(q, -t)
                time[t]=1
        else:
            heappush(q, -t)
            time[t]=1

    sorted_time=sorted(time.items(), key=lambda x:x[0])
    for _,num in sorted_time:
        answer.append(num)
    
    return answer