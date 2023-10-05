n,m=map(int,input().split())
ramp=[]
for i in range(n):
    li = list(map(int, input().split()))
    li = li[1:]
    ramp.append(li)

flag=False
for i in range(n):
    temp=ramp[:i]+ramp[i+1:]
    a=set([])
    for j in temp:
        for k in range(len(j)):
            a.add(j[k])
    if len(a)==m:
        flag=True
        break

if flag:
    print(1)
else:
    print(0)