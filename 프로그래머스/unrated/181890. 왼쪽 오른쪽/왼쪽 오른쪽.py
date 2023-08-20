def solution(str_list):
    answer = []
    
    for i, str in enumerate(str_list):
        if str == "r":
            answer = str_list[i+1:]
            break
        elif str == "l":
            answer = str_list[:i]
            break
    
    return answer