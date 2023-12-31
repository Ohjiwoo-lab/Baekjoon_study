# 골드5 - 암호 만들기

from sys import stdin
from itertools import combinations

l, c = map(int, stdin.readline().strip().split())
alpha = list(stdin.readline().strip().split())

con, gat = [], []
for a in alpha:
    if a in ['a', 'e', 'i', 'o', 'u']:
        gat.append(a)
    else:
        con.append(a)

conList = list(combinations(con, 2))
case = set()
for a, b in conList:
    nAlpha = alpha[:]
    nAlpha.remove(a)
    nAlpha.remove(b)
    for g in gat:
        nAlpha.remove(g)
        if l > 3:
            m = list(combinations(nAlpha, l-3))
            for k in m:
                tmp = [a, b, g]
                for i in k:
                    tmp.append(i)

                tmp.sort()
                s = ''
                for i in tmp:
                    s += i
                case.add(s)
        else:
            tmp = [a, b, g]
            tmp.sort()

            s = ''
            for i in tmp:
                s += i
            case.add(s)

caseList = list(case)
caseList.sort()
for s in caseList:
    print(s)