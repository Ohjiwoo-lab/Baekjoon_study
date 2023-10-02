def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

t=int(input())
for i in range(t):
    num_list=list(map(int,input().split()))
    gcd_sum=0
    for j in range(1,num_list[0]):
        for k in range(j+1,num_list[0]+1):
            if num_list[j]>=num_list[k]:
                gcd_sum+=gcd(num_list[j],num_list[k])
            else:
                gcd_sum+=gcd(num_list[k],num_list[j])
    print(gcd_sum)