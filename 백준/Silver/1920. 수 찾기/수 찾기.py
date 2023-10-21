# 실버 4 - 수 찾기

from sys import stdin

n=int(stdin.readline().strip())
a=list(map(int, stdin.readline().strip().split()))
m=int(stdin.readline().strip())
b=list(map(int, stdin.readline().strip().split()))

a.sort()
for num in b:
    i,j=0,n-1

    flag=True
    while i<=j:
        q = (i + j) // 2
        if a[q]==num:
            print(1)
            flag=False
            break
        elif a[q]>num:
            j=q-1
        else:
            i=q+1

    if flag:
        print(0)