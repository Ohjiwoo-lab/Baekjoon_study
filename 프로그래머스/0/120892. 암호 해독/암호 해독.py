def solution(cipher, code):
    answer = ''
    
    n = len(cipher)
    for i in range(n):
        if (i+1)%code == 0:
            answer += cipher[i]
    
    return answer