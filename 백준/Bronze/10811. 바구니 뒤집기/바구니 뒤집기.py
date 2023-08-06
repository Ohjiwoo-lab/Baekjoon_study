n, m = map(int, input().split())

a = [0]*n
for i in range(n):
    a[i]=i+1

for _ in range(m):
    i, j = map(int, input().split())
    a[i-1:j] = reversed(a[i-1:j])

for num in a:
    print(num, end=" ")