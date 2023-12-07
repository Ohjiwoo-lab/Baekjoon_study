def solution(k, tangerine):
    answer = 0
    
    nDict={}
    for i in tangerine:
        if nDict.get(i) is None:
            nDict[i]=1
        else:
            nDict[i]+=1
    
    sorted_dict = sorted(nDict.items(), key=lambda x:x[1], reverse=True)

    for _,cnt in sorted_dict:
        k-=cnt
        answer+=1
        if k<=0:
            break
    
    return answer