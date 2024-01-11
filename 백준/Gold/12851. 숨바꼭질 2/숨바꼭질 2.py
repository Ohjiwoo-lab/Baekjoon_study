# 골드 4 - 숨바꼭질 2

from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().strip().split())

visited = [-1]*100001

q = deque()
q.append([n, 0])
visited[n] = 0

answerTime = 0
answerCnt = 0
while q:
    lo, cnt = q.popleft()

    if lo==k:
        answerTime = cnt
        answerCnt+=1
        while q:
            lo, cnt = q.popleft()
            if lo==k and cnt==answerTime:
                answerCnt+=1

    else:
        if lo+1<=100000:
            if visited[lo+1]==-1 or visited[lo+1]>cnt:
                visited[lo + 1] = cnt+1
                q.append([lo+1, cnt+1])

        if lo-1>=0:
            if visited[lo-1]==-1 or visited[lo-1]>cnt:
                visited[lo - 1] = cnt + 1
                q.append([lo-1, cnt+1])

        if 2*lo<=100000:
            if visited[lo*2]==-1 or visited[lo*2]>cnt:
                visited[lo*2] = cnt + 1
                q.append([2*lo, cnt+1])

print(answerTime)
print(answerCnt)