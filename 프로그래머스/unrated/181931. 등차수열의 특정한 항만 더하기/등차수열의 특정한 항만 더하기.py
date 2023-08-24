def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        if included[i]:
            num = a + d*i
            answer += num
    
    return answer