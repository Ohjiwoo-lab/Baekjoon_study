def solution(n, m, section):
    answer = 0
    
    i,paint=0,len(section)
    while i!=paint:
        num=section[i]
        for j in range(i,paint):
            if num<=section[j]<num+m:
                i+=1
            else:
                break
        answer+=1
    
    return answer