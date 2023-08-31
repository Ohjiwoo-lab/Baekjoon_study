def solution(my_string, is_suffix):
    answer = 0
    
    lenth = len(is_suffix)
    my_string = my_string[len(my_string)-lenth:]
    if my_string==is_suffix:
        answer = 1
    
    return answer