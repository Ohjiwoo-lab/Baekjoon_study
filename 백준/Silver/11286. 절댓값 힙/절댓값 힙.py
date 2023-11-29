# 실버 1 - 절댓값 힙

from sys import stdin
from heapq import heappush, heappop

q=[]
n=int(stdin.readline())
for i in range(n):
    num=int(stdin.readline())
    if num==0:
        if q:
            _,origin_value=heappop(q)
            print(origin_value)
        else:
            print(0)
    else:
        heappush(q,[abs(num),num])