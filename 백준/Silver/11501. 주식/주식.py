# 실버 2 - 주식

from sys import stdin

t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    cost = list(map(int, stdin.readline().strip().split()))
    cost.reverse()

    num=0
    total_cost = 0
    for j in range(n):
        if num <= cost[j]:
            num = cost[j]
        else:
            total_cost += (num-cost[j])

    print(total_cost)