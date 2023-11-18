# 실버 2 - 풍선 공장

from sys import stdin

n, m = map(int, stdin.readline().strip().split())
time = list(map(int, stdin.readline().strip().split()))

answer = 0
left, right = 0, min(time)*m
while left <= right:
    mid = (left+right)//2

    s = 0
    for t in time:
        s += (mid//t)

    if s >= m:
        right = mid-1
        answer = mid
    else:
        left = mid+1

print(answer)