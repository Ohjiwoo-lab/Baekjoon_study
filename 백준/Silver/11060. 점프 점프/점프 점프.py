# 실버 2 - 점프 점프

from sys import stdin
from collections import deque

n = int(stdin.readline())
nmap = list(map(int, stdin.readline().strip().split()))

visited = [False]*n

q = deque()
q.append([nmap[0], 0, 0])
visited[0] = True

answer = -1
while q:
    num, cnt, idx = q.popleft()

    if idx == (n-1):
        answer = cnt
        break

    for j in range(1, num+1):
        if idx+j < n and not visited[idx+j]:
            q.append([nmap[idx+j], cnt+1, idx+j])
            visited[idx+j] = True

print(answer)