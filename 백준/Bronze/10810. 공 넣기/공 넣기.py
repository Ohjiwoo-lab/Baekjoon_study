n, m = map(int, input().split())

a = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for s in range(i-1, j):
        a[s] = k

for num in a:
    print(num, end=" ")