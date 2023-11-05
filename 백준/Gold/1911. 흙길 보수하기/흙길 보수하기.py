# 골드 5 - 흙길 보수하기

from sys import stdin

n, l=map(int, stdin.readline().strip().split())

pool = []
for i in range(n):
    pool.append(list(map(int,stdin.readline().strip().split())))

pool.sort(key=lambda x:x[0])

s, e = 0, 0
answer = 0
for a, b in pool:
    if b <= e:
        continue

    if e >= a:
        s = e
        e = s + l
    else:
        s = a
        e = s + l

    if (b - s) % l > 0:
        num = (b - s) // l + 1
    else:
        num = (b - s) // l
    answer += num

    if num>1:
        e = s + (l*num)

print(answer)