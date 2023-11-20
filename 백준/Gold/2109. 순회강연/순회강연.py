# 골드 3 - 순회강연

from sys import stdin
from heapq import heappush, heappop

n=int(stdin.readline())

lecture=[]
date=[False]*10002
for i in range(n):
    num,d=map(int, stdin.readline().strip().split())
    date[d]=True
    lecture.append([num,d])

lecture.sort(key=lambda x:(-x[1],-x[0]))

if n==0:
    print(0)
else:
    i,j=lecture[0][1],0
    answer=0
    q=[]
    while i>0:
        if not date[i]:
            if not q:
                i-=1
            else:
                answer+=(-heappop(q))
                i-=1
        else:
            num, d = lecture[j]
            if not q:
                answer+=num
            else:
                qNum=(-heappop(q))

                if qNum > num:
                    answer+=qNum
                    heappush(q, -num)
                else:
                    answer+=num
                    heappush(q, -qNum)

            for k in range(j+1,n):
                if lecture[k][1]==d:
                    heappush(q, -lecture[k][0])
                else:
                    j=k
                    break
            i-=1

    print(answer)