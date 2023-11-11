# 실버 5 - 숫자 카드

n=int(input())
nList=list(map(int,input().split()))
m=int(input())
mList=list(map(int,input().split()))

nDict={}
for i in nList:
    nDict[i]=1

for i in mList:
    if nDict.get(i) is None:
        print(0, end=" ")
    else:
        print(1, end=" ")