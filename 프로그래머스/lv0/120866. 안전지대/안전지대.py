def solution(board):
    answer = 0
    
    row = [-1,0,1,-1,1,-1,0,1]
    col = [-1,-1,-1,0,0,1,1,1]
    n = len(board[0])
    count = 0
    visited = []
    for i in range(n+2):
        temp = []
        for j in range(n+2):
            if i==0 or j==0 or i==n+1 or j==n+1:
                temp.append(True)
            else:
                temp.append(False)
        visited.append(temp)

    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i-1][j-1]==1:
                visited[i][j]=True
                count += 1
                for k in range(len(row)):
                    if not visited[i+row[k]][j+col[k]] and board[i-1+row[k]][j-1+col[k]] != 1:
                        count += 1
                        visited[i+row[k]][j+col[k]] = True

    answer = n*n - count
    
    return answer