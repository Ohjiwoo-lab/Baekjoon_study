def solution(slice, n):
    answer = 0
    
    num = n // slice
    if n % slice > 0:
        answer = num+1
    else:
        answer = num
    
    return answer