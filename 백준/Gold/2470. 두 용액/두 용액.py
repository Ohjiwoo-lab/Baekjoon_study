from sys import stdin

n=int(stdin.readline().strip())
value=list(map(int, stdin.readline().strip().split()))

value.sort()

answer=0
s,e=0,n-1
vs=[]
v=float('-inf')  # 음의 무한대

while True:
    if s>=e:
        break
    
    if value[s]+value[e]==0:
        vs=[value[s],value[e]]
        break
    elif abs(value[s]+value[e])<abs(v):
        v=value[s]+value[e]
        vs=[value[s],value[e]]
        if v<0:
            s+=1
        else:
            e-=1
    else:
        if value[s]+value[e]<0:
            s+=1
        else:
            e-=1
        
print(vs[0],vs[1])
