def solution(my_string, m, c):
    answer = ''
    
    s=[]
    for i in range(len(my_string)//m):
        s.append(my_string[m*i:m*(i+1)])
    
    for i in s:
        answer+=i[c-1]
    
    return answer