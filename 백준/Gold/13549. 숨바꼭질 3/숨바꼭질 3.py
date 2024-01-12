# 골드5 - 숨바꼭질3

from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().strip().split())

visited = [-1]*100001

q = deque()
q.append([n,0])
visited[n] = 0

answer = 0
while q:
    num, cnt = q.popleft()

    if num == k:
        answer=cnt
        while q:
            num, cnt = q.popleft()
            if num == k and answer > cnt:
                answer = cnt
        break

    if num-1>=0:
        if visited[num-1]==-1 or visited[num-1]>cnt:
            q.append([num-1, cnt + 1])
            visited[num-1] = cnt+1

    if num+1<=100000:
        if visited[num+1]==-1 or visited[num+1]>cnt:
            q.append([num+1, cnt + 1])
            visited[num+1]=cnt+1

    if num*2<=100000:
        if visited[num*2]==-1 or visited[num*2]>=cnt:
            q.append([num*2, cnt])
            visited[num*2]=cnt

print(answer)