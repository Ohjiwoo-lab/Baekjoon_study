# 실버 3 - 수열

from sys import stdin

n,k=map(int,stdin.readline().strip().split())
temper=list(map(int,stdin.readline().strip().split()))

s=0
e=s+k-1
num=sum(temper[s:e+1])
answer=num
while True:
    if (e+1) >= n:
        break
    num-=temper[s]
    num+=temper[e+1]
    if num>answer:
        answer=num

    s,e=s+1,e+1

print(answer)