import heapq
from sys import stdin

n=int(stdin.readline().strip())
h=[]
for i in range(n):
    op=int(stdin.readline().strip())
    if op==0:
        if len(h)==0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h,-op)