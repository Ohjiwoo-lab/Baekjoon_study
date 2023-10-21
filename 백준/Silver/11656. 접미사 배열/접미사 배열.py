# 실버 4 - 접미사 배열

from sys import stdin

s=stdin.readline().strip()
a=[]
for i in range(len(s)):
    a.append(s[i:])

a.sort()
for i in a:
    print(i)