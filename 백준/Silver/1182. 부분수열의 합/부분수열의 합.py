# 실버 2 - 부분수열의 합

from itertools import combinations

n, s = map(int, input().split())
num = list(map(int, input().split()))

answer = 0

for i in range(1,n+1):
    case=list(combinations(num,i))
    for j in case:
        if sum(j)==s:
            answer+=1

print(answer)