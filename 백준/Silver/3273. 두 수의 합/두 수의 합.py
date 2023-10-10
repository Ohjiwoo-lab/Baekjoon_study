from sys import stdin

n=int(stdin.readline().strip())
num_list=list(map(int,stdin.readline().strip().split()))
x=int(stdin.readline().strip())

num_list.sort()

answer=0
s,e=0,n-1

while True:
    if s>=e:
        break
    
    if num_list[s]+num_list[e]==x:
        answer+=1
        s+=1
        e-=1
    elif num_list[s]+num_list[e]<x:
        s+=1
    else:
        e-=1

print(answer)