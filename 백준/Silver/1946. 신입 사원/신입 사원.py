# 실버 1 - 신입 사원

from sys import stdin
from heapq import heappop, heappush

t=int(stdin.readline())
for _ in range(t):
    n=int(stdin.readline())
    person=[]
    for i in range(n):
        person.append(list(map(int, stdin.readline().strip().split())))

    person.sort(key=lambda x:(x[0],x[1]))

    heap=[]
    answer=0
    for i in range(n):
        heappush(heap, person[i][1])

        if i==0 or heap[0]==person[i][1]:
            answer+=1

    print(answer)