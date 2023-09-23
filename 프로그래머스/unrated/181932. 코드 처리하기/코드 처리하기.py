def solution(code):
    answer = ''
    
    mode = 0
    for i, c in enumerate(code):
        if c=="1":
            if mode==0:
                mode=1
            else:
                mode=0
            continue
        if mode==0:
            if i%2==0:
                answer += c
        if mode==1:
            if i%2!=0:
                answer += c
    
    if len(answer)==0:
        answer = "EMPTY"
    
    return answer