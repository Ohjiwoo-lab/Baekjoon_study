# 실버 1 - 봄버맨

from sys import stdin

r,c,n=map(int, stdin.readline().strip().split())
pan=[]
for i in range(r):
    tmp=[]
    for s in stdin.readline().strip():
        tmp.append(s)
    pan.append(tmp)

cnt=0
time=1
state='O'
non_state='X'
while cnt<n:
    if time==1:
        time+=1
        cnt+=1
        
    elif time==2:
        for i in range(r):
            for j in range(c):
                if pan[i][j]=='.':
                    pan[i][j]=non_state
        cnt+=1
        time+=1
        
    else:
        for i in range(r):
            for j in range(c):
                if pan[i][j]==state:
                    pan[i][j]='.'
                    if i-1>=0 and pan[i-1][j]!=state:
                        pan[i-1][j]='.'
                    if i+1<r and pan[i+1][j]!=state:
                        pan[i+1][j]='.'
                    if j-1>=0 and pan[i][j-1]!=state:
                        pan[i][j-1]='.'
                    if j+1<c and pan[i][j+1]!=state:
                        pan[i][j+1]='.'
        tmp=state
        state=non_state
        non_state=tmp
        cnt+=1
        time=2

for i in range(r):
    for j in range(c):
        if pan[i][j]=='X':
            print('O',end="")
        else:
            print(pan[i][j], end="")
    print()