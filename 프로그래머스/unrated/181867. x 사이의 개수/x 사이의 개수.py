def solution(myString):
    answer = []
    
    m = myString.split('x')
    for i in m:
        answer.append(len(i))
    
    
    return answer