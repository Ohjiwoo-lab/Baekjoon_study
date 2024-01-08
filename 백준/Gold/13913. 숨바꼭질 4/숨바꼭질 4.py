# 골드 4 - 숨바꼭질 4

from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().strip().split())

visited = [False]*100001

q = deque()
q.append([n, 0, f'{n},'])
visited[n] = True

answer = 0
route = ''
while q:
    lo, cnt, r = q.popleft()

    if lo == k:
        answer = cnt
        route = r
        break

    if lo+1<=100000 and not visited[lo+1]:
        q.append([lo+1, cnt+1, r+f'{lo+1},'])
        visited[lo+1] = True

    if lo-1>=0 and not visited[lo-1]:
        q.append([lo-1, cnt+1, r+f'{lo-1},'])
        visited[lo-1] = True

    if 2*lo<=100000 and not visited[2*lo]:
        q.append([2*lo, cnt+1, r+f'{2*lo},'])
        visited[2*lo] = True

print(answer)
for i in route.split(','):
    print(i, end=" ")