def solution(my_string, is_prefix):
    answer = 0
    
    num = len(is_prefix)
    my_string=my_string[:num]
    
    if my_string == is_prefix:
        answer = 1
    
    return answer