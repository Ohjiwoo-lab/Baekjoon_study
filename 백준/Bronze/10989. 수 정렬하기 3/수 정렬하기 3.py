from sys import stdin

n = int(stdin.readline())

a = [0 for i in range(10001)]

for i in range(n):
    num = int(stdin.readline())
    a[num] += 1

for i in range(len(a)):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)