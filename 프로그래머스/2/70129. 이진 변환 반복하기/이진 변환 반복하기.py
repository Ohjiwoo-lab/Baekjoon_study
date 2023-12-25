def solution(s):
    answer = []
    
    cnt, zero = 0,0
    while s != '1':
        one=0
        for i in s:
            if i == '1':
                one+=1
            else:
                zero+=1
        
        s = str(bin(one)[2:])
        cnt+=1
    
    answer=[cnt, zero]

    return answer