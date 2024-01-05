# 실버 1 - 나이트의 이동

from sys import stdin
from collections import deque

t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    ca, cb = map(int, stdin.readline().strip().split())
    la, lb = map(int, stdin.readline().strip().split())

    q = deque()
    q.append([ca, cb, 0])

    visited = []
    for j in range(n):
        tmp = []
        for k in range(n):
            tmp.append(False)
        visited.append(tmp)

    row = [1,2,2,1,-1,-2,-2,-1]
    col = [-2,-1,1,2,2,1,-1,-2]

    answer = 0
    while q:
        x, y, cnt = q.popleft()
        if x==la and y==lb:
            answer = cnt
            break

        for m in range(8):
            if 0<=x+col[m]<n and 0<=y+row[m]<n and not visited[x+col[m]][y+row[m]]:
                q.append([x+col[m], y+row[m], cnt+1])
                visited[x+col[m]][y+row[m]]=True

    print(answer)