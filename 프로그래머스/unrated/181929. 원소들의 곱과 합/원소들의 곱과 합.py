def solution(num_list):
    answer = 0
    
    mod = 1
    numSum = 0
    
    for num in num_list:
        mod *= num
        numSum += num
    
    if mod < numSum**2:
        answer = 1
    
    return answer