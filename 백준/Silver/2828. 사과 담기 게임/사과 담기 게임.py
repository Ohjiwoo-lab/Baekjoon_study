# 실버 5 - 사과 담기 게임

from sys import stdin

n,m=map(int, stdin.readline().strip().split())
j=int(stdin.readline())

lo=[]
for i in range(j):
    lo.append(int(stdin.readline()))

s, e = 1, 1+(m-1)
answer=0
for i in range(j):
    if s <= lo[i] <= e:
        continue

    if abs(lo[i]-s) > abs(lo[i]-e):
        answer += abs(lo[i]-e)
        s += (lo[i] - e)
        e += (lo[i] - e)
    else:
        answer += abs(lo[i] - s)
        e += (lo[i] - s)
        s += (lo[i] - s)
print(answer)