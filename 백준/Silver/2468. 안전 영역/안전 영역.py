# 실버 1 - 안전 영역

from sys import stdin
from collections import deque

def bfs(dot, region, num, n):
    q = deque()
    q.append(dot)
    region[dot[0]][dot[1]]=0

    row = [1,0,-1,0]
    col = [0,1,0,-1]

    while q:
        nDot = q.popleft()
        for i in range(4):
            if 0<=nDot[0]+col[i]<n and 0<=nDot[1]+row[i]<n and region[nDot[0]+col[i]][nDot[1]+row[i]]!=0 and region[nDot[0]+col[i]][nDot[1]+row[i]]>num:
                region[nDot[0] + col[i]][nDot[1] + row[i]]=0
                q.append([nDot[0] + col[i],nDot[1] + row[i]])
    return 1

n = int(stdin.readline())

minList, maxList = [], []
region = []
for i in range(n):
    tmp = list(map(int, stdin.readline().strip().split()))
    minList.append(min(tmp))
    maxList.append(max(tmp))
    region.append(tmp)

answer = 1
minNum, maxNum = min(minList), max(maxList)
for i in range(minNum, maxNum+1):
    cnt=0
    copyList = [arr[:] for arr in region]

    for j in range(n):
        for k in range(n):
            if copyList[j][k]!=0 and copyList[j][k]>i:
                cnt += bfs([j,k], copyList,i,n)

    if cnt >= answer:
        answer = cnt

print(answer)