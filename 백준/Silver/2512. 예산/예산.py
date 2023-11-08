# 실버 2 - 예산

from sys import stdin

n=int(stdin.readline())
request=list(map(int,stdin.readline().strip().split()))
m=int(stdin.readline())

top=max(request)
answer = 0
if n==1:
    answer=top
elif m//n >= top:
    answer=top
else:
    left,right=0,top
    while left<=right:
        mid=(left+right)//2
        if mid==0:
            answer=mid
            left=mid+1
            continue

        s=0
        for i in request:
            if mid>i:
                s+=i
            else:
                s+=mid

        if s<=m:
            answer=mid
            left=mid+1
        else:
            right=mid-1
print(answer)