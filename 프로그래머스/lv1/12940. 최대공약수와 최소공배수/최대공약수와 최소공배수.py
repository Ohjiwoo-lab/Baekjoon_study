def gcd(a, b):
    if a%b==0:
        return b
    return gcd(b,a%b)

def solution(n, m):
    answer = []
    
    if n>=m:
        gcd_num=gcd(n,m)
    else:
        gcd_num=gcd(m,n)
        
    answer=[gcd_num, n*m//gcd_num]
    
    return answer