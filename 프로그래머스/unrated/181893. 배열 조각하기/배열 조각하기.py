def solution(arr, query):
    answer = []
    
    for i, q in enumerate(query):
        if i%2 == 0:  # 짝수
            arr = arr[:q+1]
        else:  # 홀수
            arr = arr[q:]
    
    answer = arr
    
    return answer