# 실버 1 - 영역 구하기

from sys import stdin
from collections import deque

m,n,k=map(int,stdin.readline().strip().split())
nMap=[]
for i in range(m):
    tmp=[]
    for j in range(n):
        tmp.append(0)
    nMap.append(tmp)

for i in range(k):
    x1,y1,x2,y2=map(int,stdin.readline().strip().split())
    for j in range(x1,x2):
        for p in range(m-y2,m-y1):
            nMap[p][j]=1

answer=[]
q=deque()

row=[1,0,-1,0]
col=[0,1,0,-1]

def bfs(dot):
    q.append(dot)
    nMap[dot[0]][dot[1]]=1
    cnt = 1
    while q:
        nDot=q.popleft()
        for i in range(4):
            if 0<=(nDot[0]+col[i])<m and 0<=(nDot[1]+row[i])<n and nMap[nDot[0]+col[i]][nDot[1]+row[i]]==0:
                q.append([nDot[0]+col[i],nDot[1]+row[i]])
                nMap[nDot[0]+col[i]][nDot[1]+row[i]]=1
                cnt+=1
    answer.append(cnt)

for i in range(m):
    for j in range(n):
        if nMap[i][j]==0:
            bfs([i,j])

print(len(answer))
answer.sort()
for num in answer:
    print(num, end=" ")