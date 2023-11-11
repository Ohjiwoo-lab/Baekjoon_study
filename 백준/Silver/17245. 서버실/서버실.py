# 실버 2 - 서버실

from sys import stdin
from math import ceil

n=int(stdin.readline())

max_list,computer,num_sum=[],[],0
for i in range(n):
    tmp=list(map(int,stdin.readline().strip().split()))
    max_list.append(max(tmp))
    num_sum+=sum(tmp)
    computer.append(tmp)

max_num=max(max_list)
cnt=num_sum/2
answer=0
if n==1:
    answer=ceil(cnt)
else:
    left,right=0,max_num
    while left<=right:
        mid=(left+right)//2

        s=0
        for i in computer:
            for j in i:
                if (j-mid)<=0:
                    s+=j
                else:
                    s+=mid

        if s>=cnt:
            answer=mid
            right=mid-1
        else:
            left=mid+1

print(answer)