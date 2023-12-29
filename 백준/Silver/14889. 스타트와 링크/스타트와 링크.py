# 실버 1 - 스타트와 링크

from sys import stdin
from itertools import combinations

n = int(stdin.readline())
power, p = [], []
for i in range(n):
    tmp = list(map(int, stdin.readline().strip().split()))
    power.append(tmp)
    p.append(i)

case = list(combinations(p, n//2))
num = len(case)

answer = -1
for i in range(num//2):
    cnt1, cnt2 = 0, 0
    tmp1 = list(combinations(case[i], 2))
    tmp2 = list(combinations(case[num-i-1], 2))
    for b,c in tmp1:
        cnt1 += (power[b][c]+power[c][b])
    for b,c in tmp2:
        cnt2 += (power[b][c]+power[c][b])

    if answer == -1 or abs(cnt1-cnt2) < answer:
        answer = abs(cnt1-cnt2)

print(answer)