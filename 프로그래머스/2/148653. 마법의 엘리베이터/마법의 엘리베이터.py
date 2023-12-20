def solution(storey):
    answer = 0
    
    roundNum, flag = 0, False
    while storey != 0:
        remain = storey%10
        if roundNum != 0:
            remain += roundNum
            roundNum = 0
        
        if flag:
            if remain >= 5:
                remain += 1
            flag = False
            
        if remain > 5:
            roundNum = 1
            answer += (10-remain)
        elif remain == 5:
            answer += remain
            flag = True
        else:
            answer += remain
        
        storey = storey//10
    
    if roundNum != 0:
        answer += roundNum
    
    return answer