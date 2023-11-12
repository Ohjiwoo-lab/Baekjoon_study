# 실버 3 - 주유소

from sys import stdin

n=int(stdin.readline())
road=list(map(int,stdin.readline().strip().split()))
oil=list(map(int,stdin.readline().strip().split()))

oil.pop()
answer=0
i=0
while i < (n-1):
    answer+=oil[i]*road[i]

    if i < n-2:
        tmp=1
        for j in range(i+1,n-1):
            if oil[i] <= oil[j]:
                answer+=oil[i]*road[j]
                tmp+=1
            else:
                break
        i+=tmp

    else:
        break

print(answer)