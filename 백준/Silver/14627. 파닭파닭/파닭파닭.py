# 실버 2 - 파닭파닭

from sys import stdin

s,c=map(int,stdin.readline().strip().split())
p=[]
for i in range(s):
    p.append(int(stdin.readline()))

num=max(p)
left,right=0,num
answer,pa=0,0
if s==1:
    pa=num//c
else:
    while left<=right:
        mid=(left+right)//2
        if mid==0:
            pa=mid
            left=mid+1
            continue

        tmp=0
        for j in p:
            tmp+=(j//mid)

        if tmp>=c:
            pa=mid
            left=mid+1
        else:
            right=mid-1

cnt=0
for i in p:
    cnt+=i//pa
    a=i-pa*(i//pa)
    answer+=a

# 만약 파닭 개수보다 더 많이 만든 경우는 집에 가져가야하므로 추가적으로 더해준다.
if cnt>c:
    answer+=(cnt-c)*pa
print(answer)