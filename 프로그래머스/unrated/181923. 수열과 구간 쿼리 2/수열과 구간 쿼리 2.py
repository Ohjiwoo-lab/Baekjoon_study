def solution(arr, queries):
    answer = []
    
    for q in queries:
        num=[]
        for i in range(q[0], q[1]+1):
            if arr[i] > q[2]:
                num.append(arr[i])
        if len(num) == 0:
            answer.append(-1)
        else:
            answer.append(min(num))
    
    return answer