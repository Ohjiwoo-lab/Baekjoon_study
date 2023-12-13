# 실버 5 - 벚꽃이 정보섬에 피어난 이유

from sys import stdin

n=int(stdin.readline())
nList=list(map(int, stdin.readline().strip().split()))

answer=[]
for i in range(4):
    cnt=1
    for j in range(n-3):
        cnt*=nList[i+j]

    if len(answer)==0:
        answer=[i,cnt]
    else:
        if answer[1]<cnt:
            answer=[i,cnt]

print(answer[1]+sum(nList[:answer[0]]+nList[answer[0]+n-3:]))