def solution(a, b):
    answer = 0
    
    a = str(a)
    b = str(b)
    
    if int(a+b) > int(b+a):
        answer = int(a+b)
    else:
        answer = int(b+a)
    
    return answer