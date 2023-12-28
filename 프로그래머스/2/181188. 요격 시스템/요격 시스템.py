def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x:(x[0],x[1]))

    curr=[]
    for s,e in targets:
        if len(curr)==0:
            answer += 1
            curr = [s,e]
        else:
            if curr[0]<=s<curr[1]:
                if e>curr[1]:
                    curr = [s,curr[1]]
                else:
                    curr = [s,e]
            else:
                answer += 1
                curr = [s,e]
    
    return answer