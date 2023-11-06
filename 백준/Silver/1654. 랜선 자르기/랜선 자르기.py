# 실버 2 - 랜선 자르기

from sys import stdin

k,n=map(int,stdin.readline().strip().split())
lan=[]
for i in range(k):
    lan.append(int(stdin.readline()))

num=sum(lan)//n
if k==1:
    answer=num
else:
    left,right=0,num
    answer=0
    while left<=right:
        mid=(left+right)//2
        if mid==0:
            answer=mid
            left=mid+1
            continue

        s=0
        for j in lan:
            s+=j//mid
        if s<n:
            right=mid-1
        else:
            left=mid+1
            answer = mid

print(answer)