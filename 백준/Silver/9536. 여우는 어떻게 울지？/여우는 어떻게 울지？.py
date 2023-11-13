# 실버 3 - 여우는 어떻게 울지?

from sys import stdin

t=int(stdin.readline())
for i in range(t):
    record=stdin.readline().strip().split()
    ani={}
    while True:
        s=stdin.readline().strip()
        if s=="what does the fox say?":
            break
        ani[s.split()[2]]=s.split()[0]

    for re in record:
        if ani.get(re) is None:
            print(re, end=" ")