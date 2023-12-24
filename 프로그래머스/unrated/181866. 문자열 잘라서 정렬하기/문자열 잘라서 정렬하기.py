def solution(myString):
    answer = []
    
    myString = myString.split("x")
    myString.sort()
    
    for s in myString:
        if s != '':
            answer.append(s)
    
    return answer