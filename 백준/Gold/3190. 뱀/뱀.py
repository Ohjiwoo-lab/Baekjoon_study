# 골드 4 - 뱀

from sys import stdin
from collections import deque

n=int(stdin.readline())

game_map=[]
for i in range(n):
    tmp=[]
    for j in range(n):
        tmp.append(0)
    game_map.append(tmp)

game_map[0][0]=2

k=int(stdin.readline())
for i in range(k):
    x,y=map(int,stdin.readline().strip().split())
    game_map[x-1][y-1]=1

l=int(stdin.readline())
direction=deque()
for i in range(l):
    s,d=stdin.readline().strip().split()
    s=int(s)
    direction.append([s,d])

cnt=0
row=[1,0,-1,0]
col=[0,1,0,-1]
d=0
head=[0,0]
r=deque()
r.append(head)

while True:
    if direction and direction[0][0]==cnt:
        t=direction.popleft()
        if t[1]=='L':
            d=(d+3)%4
        else:
            d=(d+1)%4

    # 머리를 이동시킴
    head=[head[0]+col[d],head[1]+row[d]]
    r.append(head)

    # 벽이라면 break
    if head[0]>=n or head[0]<0:
        cnt += 1
        break
    if head[1]>=n or head[1]<0:
        cnt += 1
        break

    # 사과를 만난 경우
    if game_map[head[0]][head[1]]==1:
        game_map[head[0]][head[1]]=2
    # 지렁이를 만난경우
    elif game_map[head[0]][head[1]]==2:
        cnt += 1
        break
    # 아무것도 없는 경우
    else:
        game_map[head[0]][head[1]]=2
        tail=r.popleft()
        game_map[tail[0]][tail[1]]=0

    cnt += 1

print(cnt)