def solution(num_list, n):
    answer = []
    
    a=num_list[:n]
    b=num_list[n:]
    
    answer=b
    for i in a:
        answer.append(i)
    
    return answer