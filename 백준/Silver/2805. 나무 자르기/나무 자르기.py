# 실버 2 - 나무 자르기

from sys import stdin

def cal(left,right,tree,n,m):
    a = 0
    while left<=right:
        mid=(left+right)//2

        s=0
        for i in tree:
            if i-mid>0:
                s+=(i-mid)

        if s==m:
            a=mid
            break
        elif s > m:
            a=mid
            left = mid + 1
        else:
            right = mid - 1

    return a

n,m=map(int,stdin.readline().strip().split())
tree=list(map(int,stdin.readline().strip().split()))

left,right=1,max(tree)
answer=0
if n==1:
    answer=right-m
elif m==0:
    answer=right
else:
    answer=cal(left,right,tree,n,m)

print(answer)