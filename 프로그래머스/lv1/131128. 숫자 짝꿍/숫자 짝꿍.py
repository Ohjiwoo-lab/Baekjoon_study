def solution(X, Y):
    answer = ''
    
    x_dict, y_dict = {}, {}
    for i in X:
        if x_dict.get(i) is None:
            x_dict[i] = 1
        else:
            x_dict[i] += 1
    
    for i in Y:
        if y_dict.get(i) is None:
            y_dict[i] = 1
        else:
            y_dict[i] += 1
    
    num_list = []
    for num, cnt in x_dict.items():
        if y_dict.get(num) is None:
            continue
        for i in range(min(cnt, y_dict[num])):
            num_list.append(num)
    
    if len(num_list)==0:
        answer="-1"
    elif num_list[0]=='0':
        answer="0"
    else:
        num_list.sort(reverse=True)
        for num in num_list:
            answer+=num
    
    return answer