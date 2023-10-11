n=int(input())
std=[]
for i in range(n):
    std.append(input())

m=len(std[0])
k=0
for i in range(m-1,-1,-1):
    temp=set()
    for j in range(n):
        temp.add(std[j][i:])
    if len(temp)==n:
        k=m-i
        break

print(k)