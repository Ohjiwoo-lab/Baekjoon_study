# 골드 2 - 컵라면

from sys import stdin
from heapq import heappush, heappop

n=int(stdin.readline())
cup=[]
date=[False]*(n+1)
for i in range(n):
    d,num=list(map(int,stdin.readline().strip().split()))
    date[d]=True
    cup.append([d,num])

cup.sort(key=lambda x:(-x[0],-x[1]))

q=[]
answer=0
i,j=n,0
while i>0:
    if not date[i]:
        if not q:
            i-=1
        else:
            answer+=(-heappop(q))
            i-=1
    else:
        tmpD, num = cup[j]
        if not q:
            answer+=num
        else:
            tmpN = -heappop(q)

            if tmpN > num:
                answer += tmpN
                heappush(q, -num)
            else:
                answer += num
                heappush(q, -tmpN)

        for k in range(j + 1, n):
            if cup[k][0] == tmpD:
                heappush(q, -cup[k][1])
            else:
                j = k
                break
        i-=1

print(answer)