from sys import stdin

a, b = map(list, stdin.readline().split())
a = list(map(int, a))
b = list(map(int, b))

a_sum = sum(a)
num = 0
for j in b:
    num += a_sum*j

print(num)