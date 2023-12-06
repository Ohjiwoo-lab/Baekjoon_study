def solution(s):
    answer = []
    
    sList = []
    for i in s.split(','):
        i=i.lstrip('{')
        i=i.rstrip('}')
        sList.append(int(i))
    
    num_dict={}
    for i in sList:
        if num_dict.get(i) is None:
            num_dict[i]=1
        else:
            num_dict[i]+=1
    
    sorted_dict = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
    
    for digit, _ in sorted_dict:
        answer.append(digit)
    
    return answer