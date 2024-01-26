def solution(strArr):
    answer = 0
    
    nDict = {}
    for s in strArr:
        if nDict.get(len(s)) is not None:
            nDict[len(s)] += 1
        else:
            nDict[len(s)] = 1
    
    sorted_dict = sorted(nDict.items(), key=lambda x:-x[1])
    answer = sorted_dict[0][1]
    
    return answer