# 로프

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()
weight = [0 for _ in range(N)]
for i in range(N):
    weight[i] = arr.pop(0) * (N - i)

print(max(weight))
