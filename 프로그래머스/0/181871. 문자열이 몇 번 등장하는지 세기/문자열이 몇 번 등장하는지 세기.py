def solution(myString, pat):
    answer = 0
    
    n = len(myString)
    for i in range(n):
        flag = True
        if myString[i]==pat[0]:
            for j in range(1, len(pat)):
                if i+j>=n or myString[i+j]!=pat[j]:
                    flag = False
                    break
            if flag:
                answer+=1
    
    return answer