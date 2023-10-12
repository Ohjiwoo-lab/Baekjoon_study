from sys import stdin

n=int(stdin.readline().strip())
line=[]
for i in range(n):
    line.append(list(map(int,stdin.readline().strip().split())))

line.sort(key=lambda x:x[0])

dot1,dot2=line[0][0],line[0][1]
line=line[1:]
answer=0
for s,e in line:
    if s>dot2:
        answer+=(dot2-dot1)
        dot1=s
        dot2=e
    else:
        dot2=max(dot2,e)

answer+=(dot2-dot1)
print(answer)