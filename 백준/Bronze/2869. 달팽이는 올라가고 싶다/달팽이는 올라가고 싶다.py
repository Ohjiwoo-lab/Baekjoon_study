from sys import stdin

a, b, v = map(int, stdin.readline().split())

aim = v - a

if aim % (a-b)==0:
    day = aim//(a-b)
else:
    day = aim//(a-b) + 1

print(day+1)