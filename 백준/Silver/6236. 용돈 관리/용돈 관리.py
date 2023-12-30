# 실버 2 - 용돈 관리

from sys import stdin

n, m = map(int, stdin.readline().strip().split())
cost = []
for i in range(n):
    cost.append(int(stdin.readline()))

answer = 0

s, e = max(cost), sum(cost)
while s <= e:
    mid = (s+e)//2

    cnt, curr = 1, mid
    for i in cost:
        if curr >= i:
            curr -= i
        else:
            cnt += 1
            curr = mid
            curr -= i

    if cnt <= m:
        answer = mid
        e = mid - 1
    else:
        s = mid + 1

print(answer)