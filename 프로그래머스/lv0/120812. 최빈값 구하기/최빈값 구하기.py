def solution(array):
    answer = 0
    
    num_dict = {}
    for i in array:
        if num_dict.get(i) is None:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    
    max_num = max(list(num_dict.values()))
    max_list = []
    for i in array:
        if num_dict[i]==max_num:
            max_list.append(i)
            

    if len(set(max_list))>1:
        answer=-1
    else:
        answer=max_list[0]
    
    return answer