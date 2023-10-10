from sys import stdin

n=int(stdin.readline())
m=int(stdin.readline())
material=list(map(int,stdin.readline().strip().split()))

material.sort()

answer=0
s,e=0,n-1
while True:
    if s>=e:
        break
    
    if material[s]+material[e]==m:
        answer+=1
        s+=1
        e-=1
    elif material[s]+material[e]<m:
        s+=1
    else:
        e-=1

print(answer)