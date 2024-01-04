# 실버 2 - 숫자판 점프(dfs)

from sys import stdin

def dfs(nmap, dot, s, num):
    row = [1, 0, -1, 0]
    col = [0, 1, 0, -1]

    s += nmap[dot[0]][dot[1]]
    if len(s)==6:
        num.add(s)
        return

    for i in range(4):
        if 0<=dot[0]+col[i]<5 and 0<=dot[1]+row[i]<5:
            dfs(nmap, [dot[0]+col[i],dot[1]+row[i]], s, num)

nmap = []
for i in range(5):
    tmp = list(stdin.readline().strip().split())
    nmap.append(tmp)

num = set()
for i in range(5):
    for j in range(5):
        s = ''
        dfs(nmap, [i, j], s, num)

answer = len(num)
print(answer)