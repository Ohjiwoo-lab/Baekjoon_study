# 실버 2 - 결혼식

from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

f = set()
fDict = {}
for i in range(m):
    t = list(map(int, stdin.readline().strip().split()))
    if t[0] == 1:
        f.add(t[1])
    else:
        if fDict.get(t[0]) is not None:
            fDict[t[0]].append(t[1])
        else:
            fDict[t[0]] = [t[1]]

        if fDict.get(t[1]) is not None:
            fDict[t[1]].append(t[0])
        else:
            fDict[t[1]] = [t[0]]

lf = list(f)
for i in lf:
    if fDict.get(i) is not None:
        for j in fDict[i]:
            f.add(j)

print(len(f))