# 골드 5 - 장군

from sys import stdin
from collections import deque

r1,c1=map(int,stdin.readline().strip().split())
r2,c2=map(int,stdin.readline().strip().split())

q=deque()
row=[2,3,3,2,-2,-3,-3,-2]
col=[-3,-2,2,3,3,2,-2,-3]

visited=[]
for i in range(10):
    tmp=[]
    for j in range(9):
        tmp.append(False)
    visited.append(tmp)

visited[r1][c1]=True
q.append([[r1,c1],0])

answer=-1
flag=False
while q:
    dot,cnt=q.popleft()
    for i in range(8):
        nDot = [dot[0] + col[i], dot[1] + row[i]]
        if 0 <= nDot[0] <= 9 and 0 <= nDot[1] <= 8 and not visited[nDot[0]][nDot[1]]:
            c,r=col[i],row[i]
            # 한 번 갔을 때
            if abs(r)<abs(c):
                tDot=[dot[0]+c//3,dot[1]]
                if c<0:
                    c+=1
                else:
                    c-=1
            else:
                tDot=[dot[0],dot[1]+(r // 3)]
                if r<0:
                    r+=1
                else:
                    r-=1

            if tDot[0]==r2 and tDot[1]==c2:
                continue

            # 두 번 갔을 때
            tDot=[tDot[0]+c//2,tDot[1]+r//2]
            if tDot[0] == r2 and tDot[1] == c2:
                continue

            # 최종 목적지 도착했을 때
            if nDot[0]==r2 and nDot[1]==c2:
                answer=cnt+1
                flag=True
                break
            else:
                q.append([[nDot[0],nDot[1]],cnt+1])
                visited[nDot[0]][nDot[1]]=True

    if flag:
        break

print(answer)