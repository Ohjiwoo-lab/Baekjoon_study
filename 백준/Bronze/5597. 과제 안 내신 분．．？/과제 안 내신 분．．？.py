a = [0] * 30

for _ in range(28):
    n = int(input())
    a[n-1] = 1

for i, num in enumerate(a):
    if num == 0:
        print(i+1)