def solution(arr, queries):
    answer = arr
    
    for q in queries:
        i, j = q[0], q[1]
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    return answer