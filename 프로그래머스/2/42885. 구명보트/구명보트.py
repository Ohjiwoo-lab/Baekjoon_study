from heapq import heappush, heappop

def solution(people, limit):
    answer = 1
    
    people.sort(reverse=True)
    
    q=[]
    heappush(q,-(limit-people[0]))
    for i in range(1,len(people)):
        if q:
            if -q[0] < people[i]:
                answer+=1
                heappush(q, -(limit-people[i]))
            else:
                num=-heappop(q)
        else:
            answer+=1
            heappush(q, -(limit-people[i]))
    
    return answer