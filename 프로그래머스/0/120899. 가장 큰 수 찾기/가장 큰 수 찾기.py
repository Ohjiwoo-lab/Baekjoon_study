def solution(array):
    answer = []
    
    idx = 0
    num = array[0]
    
    for i in range(1, len(array)):
        if array[i]>num:
            num=array[i]
            idx=i
    
    answer=[num,idx]
    
    return answer