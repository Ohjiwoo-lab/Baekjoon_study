# 골드 5 - 최소 회의실 개수

from sys import stdin
from heapq import heappush, heappop

n=int(stdin.readline())
con=[]
for i in range(n):
    con.append(list(map(int, stdin.readline().strip().split())))

con.sort(key=lambda x:(x[0],x[1]))

answer=0
room=[]
for s,e in con:
    if len(room)==0:
        answer+=1
        heappush(room, e)
    else:
        if s<room[0]:
            answer+=1
            heappush(room, e)
        else:
            ts = heappop(room)
            heappush(room, e)

print(answer)