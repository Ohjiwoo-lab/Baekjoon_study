def solution(s):
    answer = ''
    
    num = list(map(int, s.split()))
    num.sort()
    
    answer = f'{num[0]} {num[-1]}'
    
    return answer