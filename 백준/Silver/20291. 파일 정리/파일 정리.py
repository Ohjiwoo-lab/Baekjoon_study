# 실버 3 - 파일 정리

from sys import stdin

n=int(stdin.readline())

ext={}
for i in range(n):
    name=stdin.readline().strip().split('.')[1]
    if ext.get(name) is None:
        ext[name]=1
    else:
        ext[name]+=1

sort_ext=sorted(ext.items(), key=lambda x:x[0])

for key,value in sort_ext:
    print(key, value)