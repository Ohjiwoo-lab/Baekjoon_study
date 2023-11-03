def solution(arr, intervals):
    answer = []
    
    for s,e in intervals:
        a=arr[s:e+1]
        for i in a:
            answer.append(i)
    
    return answer