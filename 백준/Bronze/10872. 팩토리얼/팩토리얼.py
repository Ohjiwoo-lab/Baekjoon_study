from sys import stdin

n = int(stdin.readline())

if n == 0:
    print(1)
else:
    num = 1
    for i in range(1, n+1):
        num *= i
    print(num)