def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    a,b = denom1, denom2
    
    numer1 *= b
    denom1 *= b
    numer2 *= a
    denom2 *= a
    
    nNum = numer1 + numer2
    nDen = denom1
    
    c, d = nNum, nDen
    while d > 0:
        c, d = d, c%d
    
    answer.append(nNum//c)
    answer.append(nDen//c)
    
    return answer