# 실버 5 - UCPC는 무엇의 약자일까?

from sys import stdin

s = stdin.readline().strip()

cnt=0
for i in s:
    if i=='U' and cnt==0:
        cnt+=1
    if i=='C' and (cnt==1 or cnt==3):
        cnt+=1
    if i=='P' and cnt==2:
        cnt+=1

if cnt==4:
    print("I love UCPC")
else:
    print("I hate UCPC")