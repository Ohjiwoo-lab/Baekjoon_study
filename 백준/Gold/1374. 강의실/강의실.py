# 골드 5 - 강의실

from sys import stdin
from heapq import heappush, heappop

n=int(stdin.readline())

lecture=[]
for i in range(n):
    lecture.append(list(map(int,stdin.readline().strip().split())))

# 강의 시작시간을 기준으로 정렬
lecture.sort(key=lambda x:x[1])

q=[]
heappush(q, lecture[0][2])
answer=1
for i in range(1, n):
    time=heappop(q)
    if time<=lecture[i][1]:
        heappush(q,lecture[i][2])
    else:
        heappush(q, time)
        answer+=1
        heappush(q, lecture[i][2])

print(answer)