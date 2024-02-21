def solution(myString, pat):
    answer = 0
    
    s = ''
    for i in myString:
        if i=='A':
            s += 'B'
        if i=='B':
            s += 'A'
    
    if pat in s:
        answer = 1
    
    return answer