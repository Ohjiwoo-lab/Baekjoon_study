def solution(participant, completion):
    answer = ''
    
    name_dict = {}
    for i in participant:
        if name_dict.get(i) is None:
            name_dict[i] = 1
        else:
            name_dict[i] += 1
    
    for i in completion:
        name_dict[i] -= 1
        if name_dict[i]==0:
            del name_dict[i]
            
    answer = list(name_dict.keys())[0]
    
    return answer