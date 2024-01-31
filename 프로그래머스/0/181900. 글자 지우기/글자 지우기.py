from collections import deque

def solution(my_string, indices):
    answer = ''
    
    indices.sort()
    a = deque(indices)
    for i in range(len(my_string)):
        if a and i==a[0]:
            a.popleft()
        else:
            answer+=my_string[i]
    
    return answer