def solution(a, b):
    answer = 0
    
    mul = 2*a*b
    con = int(str(a)+str(b))
    
    if mul > con:
        answer = mul
    else:
        answer = con
    
    return answer