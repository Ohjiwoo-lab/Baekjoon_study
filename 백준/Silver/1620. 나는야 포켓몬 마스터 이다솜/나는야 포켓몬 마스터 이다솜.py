from sys import stdin

n, m = map(int, stdin.readline().split())

pok_name = {}
rev_pok = {}

for i in range(n):
    name = stdin.readline().strip()
    pok_name[name] = i+1
    rev_pok[i+1] = name

for _ in range(m):
    a = stdin.readline().strip()
    if a.isdigit():
        print(rev_pok[int(a)])
    else:
        print(pok_name[a])