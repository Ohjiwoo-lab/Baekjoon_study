# 실버 4 - 국영수

from sys import stdin

n=int(stdin.readline().strip())
s=[]
for i in range(n):
    tmp=list(stdin.readline().strip().split())
    tmp[1]=int(tmp[1])
    tmp[2] = int(tmp[2])
    tmp[3] = int(tmp[3])
    s.append([tmp[0],tmp[1],tmp[2],tmp[3]])

s.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in s:
    print(i[0])