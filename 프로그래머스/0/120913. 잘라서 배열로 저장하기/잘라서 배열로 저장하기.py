def solution(my_str, n):
    answer = []
    
    num = len(my_str)
    str = ''
    for i in range(num):
        str += my_str[i]
        if (i+1)%n == 0:
            answer.append(str)
            str = ''
            
    if len(str)!=0:
        answer.append(str)
    
    return answer