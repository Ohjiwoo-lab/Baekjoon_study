from heapq import heappush, heappop

def solution(book_time):
    answer = 0
    
    book_time.sort(key=lambda x: (x[0],x[1]))
    
    q=[]
    heappush(q, book_time[0][1])
    answer+=1
    
    for start,end in book_time[1:]:
        # 가장 시간이 짧은 객실
        t=heappop(q)
        t_time=int(t.split(':')[0])
        t_minute=int(t.split(':')[1])+10
        
        if t_minute>=60:
            t_time+=1
            t_minute-=60
        
        # 받으려는 손님
        s_time=int(start.split(':')[0])
        s_minute=int(start.split(':')[1])
        
        if (t_time*60+t_minute) <= (s_time*60+s_minute):
            heappush(q, end)
        else:
            heappush(q, t)
            heappush(q, end)
            answer+=1
    
    return answer