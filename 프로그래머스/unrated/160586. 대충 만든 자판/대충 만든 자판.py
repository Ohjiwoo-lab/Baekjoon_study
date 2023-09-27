def solution(keymap, targets):
    answer = []
    
    for key in targets:
        min_num, flag = [], False
        for s in key:
            num = []
            for i in keymap:
                index=i.find(s)
                if index != -1:
                    num.append(index+1)
            
            if len(num)==0:
                answer.append(-1)
                flag=True
                break
            else:
                min_num.append(min(num))

        if not flag:
            answer.append(sum(min_num))
    
    return answer