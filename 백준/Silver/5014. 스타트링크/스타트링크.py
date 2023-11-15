# 실버 1 - 스타트링크

from sys import stdin
from collections import deque

f,s,g,u,d=map(int, stdin.readline().strip().split())

answer=-1
if s>g and d==0:
    answer=-1
elif s<g and u==0:
    answer=-1
else:
    q = deque()
    visited=[False] * (f+1)

    # 시작점 방문체크
    q.append([0, s])
    visited[s]=True

    while q:
        cnt, num=q.popleft()
        if num==g:
            answer=cnt
            break

        if (num+u)<=f and not visited[num+u]:
            q.append([cnt+1, num+u])
            visited[num+u]=True

        if (num-d)>0 and not visited[num-d]:
            q.append([cnt+1, num-d])
            visited[num-d] = True

if answer==-1:
    print("use the stairs")
else:
    print(answer)