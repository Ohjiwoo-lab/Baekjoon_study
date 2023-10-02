def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a>=b:
        gcd_num=gcd(a,b)
    else:
        gcd_num=gcd(b,a)
    print(a*b//gcd_num)