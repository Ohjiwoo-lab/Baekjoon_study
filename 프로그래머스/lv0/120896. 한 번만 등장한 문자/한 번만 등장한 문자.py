def solution(s):
    answer = ''
    
    str_list = []
    str_dict = {}
    for i in s:
        if str_dict.get(i) is None:
            str_dict[i] = 1
        else:
            str_dict[i] += 1
    
    for i, num in str_dict.items():
        if num == 1:
            str_list.append(i)
    
    str_list.sort()
    for i in str_list:
        answer += i
    
    return answer