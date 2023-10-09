n,k=map(int,input().split())

cnt,flag=0,False
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        flag=True
        break

if not flag:
    print(0)