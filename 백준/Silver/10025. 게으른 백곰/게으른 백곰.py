# 실버 3 - 게으른 백곰
from sys import stdin

n,k=map(int,stdin.readline().strip().split())
ice=[]
for i in range(n):
    ice.append(list(map(int,stdin.readline().strip().split())))

ice.sort(key=lambda x:x[1])

num=ice[-1][1]+1
ice_list=[0]*num

for g,x in ice:
    ice_list[x]=g

d=2*k+1
s=ice[0][1]
e=s+d-1
num_sum=sum(ice_list[s:e+1])
answer=num_sum
while True:
    if (e+1)>=num:
        break

    num_sum-=ice_list[s]
    num_sum+=ice_list[e+1]
    if num_sum>answer:
        answer=num_sum

    s,e=s+1,e+1

print(answer)