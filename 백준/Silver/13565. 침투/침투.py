# 실버 2 - 침투

from sys import stdin
from collections import deque

def bfs(nmap, dot, n, m):
    q = deque()
    q.append(dot)
    nmap[dot[0]][dot[1]] = '1'

    row = [1,0,-1,0]
    col = [0,1,0,-1]
    while q:
        x, y = q.popleft()
        for j in range(4):
            if 0<=x+col[j]<n and 0<=y+row[j]<m and nmap[x+col[j]][y+row[j]]=='0':
                if x+col[j]==(n-1):
                    return 1
                q.append([x+col[j], y+row[j]])
                nmap[x + col[j]][y + row[j]] = '1'

    return 0

nmap = []
n, m = map(int, stdin.readline().strip().split())
for i in range(n):
    tmp = list(stdin.readline().strip())
    nmap.append(tmp)

answer = 'NO'
for i in range(m):
    if nmap[0][i]=='0':
        result = bfs(nmap, [0,i], n, m)
        if result == 1:
            answer = "YES"
            break

print(answer)