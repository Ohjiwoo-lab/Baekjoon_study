def solution(sequence, k):
    answer = []
    
    n=len(sequence)
    
    s,e=0,0
    num=sequence[0]
    while s<=e:
        # k보다 작은 경우 (end를 이동시켜 값을 늘린다.)
        if num < k:
            if (e+1)>=n:
                break
            else:
                e+=1
            num+=sequence[e]
            
        # k보다 큰 경우 (start를 이동시켜 값을 줄인다.)
        elif num > k:
            num-=sequence[s]
            s+=1
        
        # k랑 같은 경우
        else:
            if len(answer)==0:
                answer=[s,e]
            else:
                if (answer[1]-answer[0])>(e-s):
                    answer=[s,e]
                elif (answer[1]-answer[0])==(e-s):
                    if answer[0]>s:
                        answer=[s,e]
            
            if (s+1)>=n:
                break
            
            num-=sequence[s]
            s+=1
    
    return answer