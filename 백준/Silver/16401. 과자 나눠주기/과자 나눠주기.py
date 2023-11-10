# 실버 2 - 과자 나눠주기

from sys import stdin

m,n=map(int,stdin.readline().strip().split())
snack=list(map(int,stdin.readline().strip().split()))

num=max(snack)

answer=0
if m==1:
    answer=num
elif n==1:
    answer=snack[0]//m
else:
    left,right=0,num
    while left<=right:
        mid=(left+right)//2
        if mid==0:
            answer=mid
            left=mid+1
            continue

        cnt=0
        for s in snack:
            cnt+=(s//mid)

        if cnt>=m:
            answer=mid
            left=mid+1
        else:
            right=mid-1

print(answer)