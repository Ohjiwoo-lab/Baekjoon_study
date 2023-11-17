# 실버 2 - 방탈출

from sys import stdin

n=int(stdin.readline())
nList=list(map(int,stdin.readline().strip().split()))

s=[0]*n
answer=0
for i in range(n):
    if nList[i]!=s[i]:
        answer+=1
        s[i]=1-s[i]
        if i+1<n:
            s[i+1]=1-s[i+1]
        if i+2<n:
            s[i+2]=1-s[i+2]

print(answer)