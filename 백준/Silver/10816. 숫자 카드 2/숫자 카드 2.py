# 실버 4 - 숫자 카드 2

from sys import stdin

n=int(stdin.readline())
nList=list(map(int, stdin.readline().strip().split()))
m=int(stdin.readline())
mList=list(map(int, stdin.readline().strip().split()))

nDict={}
for i in nList:
    if nDict.get(i) is None:
        nDict[i]=1
    else:
        nDict[i]+=1

for i in mList:
    if nDict.get(i) is not None:
        print(nDict[i], end=" ")
    else:
        print(0, end=" ")