# 실버 2 - 최소 힙

from sys import stdin
from heapq import heappush, heappop

q=[]
n=int(stdin.readline())
for i in range(n):
    num=int(stdin.readline())
    if num>0:
        heappush(q,num)
    elif num==0:
        if q:
            print(heappop(q))
        else:
            print(0)