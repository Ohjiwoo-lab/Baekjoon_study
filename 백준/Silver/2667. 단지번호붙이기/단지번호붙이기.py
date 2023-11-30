# 실버 1 - 단지 번호 붙이기

from sys import stdin
from collections import deque

n = int(stdin.readline())
nMap = []
for i in range(n):
    t = list(stdin.readline().strip())
    nMap.append(list(map(int, t)))

answer=[]
q=deque()

row=[-1,0,1,0]
col=[0,-1,0,1]

def bfs(dot):
    cnt=1
    q.append(dot)
    nMap[dot[0]][dot[1]] = 0
    while q:
        x,y=q.popleft()
        if 0<=(x+col[0])<n and 0<=(y+row[0])<n and nMap[x+col[0]][y+row[0]]==1:
            q.append([x+col[0],y+row[0]])
            nMap[x+col[0]][y+row[0]] = 0
            cnt+=1
        if 0<=(x+col[1])<n and 0<=(y+row[1])<n and nMap[x+col[1]][y+row[1]]==1:
            q.append([x+col[1],y+row[1]])
            nMap[x+col[1]][y+row[1]] = 0
            cnt += 1
        if 0<=(x+col[2])<n and 0<=(y+row[2])<n and nMap[x+col[2]][y+row[2]]==1:
            q.append([x+col[2],y+row[2]])
            nMap[x+col[2]][y+row[2]] = 0
            cnt += 1
        if 0<=(x+col[3])<n and 0<=(y+row[3])<n and nMap[x+col[3]][y+row[3]]==1:
            q.append([x+col[3],y+row[3]])
            nMap[x+col[3]][y+row[3]] = 0
            cnt += 1
    answer.append(cnt)

for i in range(n):
    for j in range(n):
        if nMap[i][j]==1:
            bfs([i,j])

answer.sort()
print(len(answer))
for i in answer:
    print(i)