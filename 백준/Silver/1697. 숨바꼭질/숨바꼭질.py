# 실버 1 - 숨바꼭질

from sys import stdin
from collections import deque

n,k=map(int, stdin.readline().strip().split())

visited = [False]*100001

q=deque()
q.append([n,0])
visited[n]=True

answer = -1
while q:
    lo, cnt = q.popleft()

    if lo==k:
        answer = cnt
        break

    if lo+1<=100000 and not visited[lo+1]:
        q.append([lo+1, cnt+1])
        visited[lo+1]=True

    if lo-1>=0 and not visited[lo-1]:
        q.append([lo-1, cnt+1])
        visited[lo-1]=True

    if lo*2<=100000 and not visited[lo*2]:
        q.append([lo*2, cnt+1])
        visited[lo*2]=True

print(answer)