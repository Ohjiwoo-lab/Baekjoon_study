from sys import stdin

n = int(stdin.readline())

fibbo = [0,1]
for i in range(1,n):
    fibbo.append(fibbo[i-1]+fibbo[i])

print(fibbo[n])