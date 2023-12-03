from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    case=list(permutations(dungeons,len(dungeons)))
    
    for i in case:
        b,cnt=k,0
        for j,m in i:
            if j<=b:
                b-=m
                cnt+=1
        if cnt>answer:
            answer=cnt
    
    return answer