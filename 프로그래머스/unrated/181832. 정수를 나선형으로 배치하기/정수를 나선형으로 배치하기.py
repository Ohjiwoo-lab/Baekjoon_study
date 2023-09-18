def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        answer.append(temp)
    
    i,j,num=0,0,1
    state=1
    while True:
        answer[i][j]=num
        if num==n*n:
            break
        num += 1

        if state==1:
            if (j+1)==n or answer[i][j+1] != 0:
                state=2
                i+=1
            else:
                j+=1
        elif state==2:
            if (i+1)==n or answer[i+1][j] != 0:
                state=3
                j-=1
            else:
                i+=1
        elif state==3:
            if (j-1)==-1 or answer[i][j-1] != 0:
                state=4
                i-=1
            else:
                j-=1
        elif state==4:
            if (i-1)==-1 or answer[i-1][j] != 0:
                state=1
                j+=1
            else:
                i-=1
    
    return answer
