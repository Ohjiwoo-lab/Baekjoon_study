# 실버 3 - 문자열 집합

from sys import stdin

n,m=map(int,stdin.readline().strip().split())
s={}
for i in range(n):
    name=stdin.readline().strip()
    s[name] = 1

answer=0
for i in range(m):
    name = stdin.readline().strip()
    if s.get(name) is not None:
        answer+=1

print(answer)