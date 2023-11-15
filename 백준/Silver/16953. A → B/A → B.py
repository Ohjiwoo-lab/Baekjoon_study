# 실버 2 - A->B
# 다시 수가 작아지는 경우가 없으므로 방문 처리 불필요

from sys import stdin
from collections import deque

a,b=map(int, stdin.readline().strip().split())

q=deque()
q.append([0,a])
answer=-2
while q:
    cnt,num=q.popleft()
    if num==b:
        answer=cnt
        break

    if num*2<=b:
        q.append([cnt+1,num*2])

    tmp = int(str(num)+'1')
    if tmp<=b:
        q.append([cnt+1,tmp])

print(answer+1)