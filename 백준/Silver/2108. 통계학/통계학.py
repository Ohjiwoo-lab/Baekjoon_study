# 실버 3 - 통계학

from sys import stdin
from collections import Counter

n=int(stdin.readline().strip())
num=[]
for i in range(n):
    num.append(int(stdin.readline().strip()))

a=sum(num)/n
print(int(round(a,0)))

num.sort()
print(num[(n-1)//2])

s=Counter(num).most_common()
max_num=s[0][1]
tmp=[]
for k,cnt in s:
    if cnt==max_num:
        tmp.append(k)

if len(tmp)==1:
    print(tmp[0])
else:
    print(tmp[1])

print(num[n-1]-num[0])