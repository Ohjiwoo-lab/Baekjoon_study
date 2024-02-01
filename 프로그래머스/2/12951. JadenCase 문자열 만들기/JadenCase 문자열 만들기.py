def solution(s):
    answer = ''
    
    flag = True
    for i in s:
        if i==' ':
            answer += i
            flag = True
        elif i.isalpha():
            if flag:
                answer += i.upper()
                flag = False
            else:
                answer += i.lower()
        else:
            answer += i
            flag = False
    
    return answer