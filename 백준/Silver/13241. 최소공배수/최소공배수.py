from sys import stdin

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

a,b=map(int, stdin.readline().strip().split())
if a>b:
    print(a*b//gcd(a,b))
else:
    print(a*b//gcd(b,a))