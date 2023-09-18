def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        answer.append(temp)
    
    row = [1,0,-1,0]
    col = [0,1,0,-1]
    
    i,j,num=0,0,1
    state=1
    while True:
        answer[i][j]=num
        if num==n*n:
            break
        num += 1
        
#         i=i+row[state]
#         j=j+col[state]
        
#         if i<0 or i==n or j<0 or j==n:
#             state=(state+1)%4
            
#         if answer[i+row[state]][j+col[state]] != 0:
#             state=(state+1)%4

        if state==1:
            j+=1
            if j==n:
                state=2
                j-=1
                i+=1
            elif answer[i][j] != 0:
                state=2
                j-=1
                i+=1
        elif state==2:
            i+=1
            if i==n:
                state=3
                i-=1
                j-=1
            elif answer[i][j] != 0:
                state=3
                i-=1
                j-=1
        elif state==3:
            j-=1
            if j<0:
                state=4
                j+=1
                i-=1
            elif answer[i][j] != 0:
                state=4
                j+=1
                i-=1
        elif state==4:
            i-=1
            if i<0:
                state=1
                i+=1
                j+=1
            elif answer[i][j] != 0:
                state=1
                i+=1
                j+=1
    
    return answer