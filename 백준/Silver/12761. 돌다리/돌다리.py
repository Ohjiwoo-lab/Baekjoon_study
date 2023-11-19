# 실버 1 - 돌다리

from sys import stdin
from collections import deque

a, b, n, m=map(int,stdin.readline().strip().split())

q=deque()
visited=[0]*100001
q.append([0,n])
visited[n]=True

answer=0
while q:
    cnt, num = q.popleft()

    if num==m:
        answer=cnt
        break

    # +1
    if (num+1)<=100000 and not visited[num+1]:
        q.append([cnt+1, num+1])
        visited[num+1] = True
    # -1
    if (num-1)>=0 and not visited[num-1]:
        q.append([cnt+1, num-1])
        visited[num-1] = True

    # +a
    if (num+a)<=100000 and not visited[num+a]:
        q.append([cnt+1, num+a])
        visited[num+a] = True
    # -a
    if (num-a)>=0 and not visited[num-a]:
        q.append([cnt+1, num-a])
        visited[num-a] = True

    # +b
    if (num+b)<=100000 and not visited[num+b]:
        q.append([cnt+1, num+b])
        visited[num+b] = True
    # -b
    if (num-b)>=0 and not visited[num-b]:
        q.append([cnt+1, num-b])
        visited[num-b] = True

    # a배
    if (num*a)<=100000 and not visited[num*a]:
        q.append([cnt+1, num*a])
        visited[num*a] = True
    # b배
    if (num*b)<=100000 and not visited[num*b]:
        q.append([cnt+1, num*b])
        visited[num*b] = True

print(answer)