def solution(id_list, report, k):
    answer = []
    
    user_dict,count_dict={},{}
    for id in id_list:
        user_dict[id]=[]
        count_dict[id]=0

    report = set(report)
    for i in report:
        a,b = i.split()
        user_dict[b].append(a)
        
    for _, name in user_dict.items():
        if len(name)<k:
            continue
        for n in name:
            count_dict[n]+=1
    
    answer = list(count_dict.values())
    
    return answer