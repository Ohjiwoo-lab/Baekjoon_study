from collections import deque

def solution(board):
    answer = -1
    
    n=len(board)
    m=len(board[0])
    
    dot = []
    visited=[]
    flag = False
    for i in range(n):
        tmp = []
        for j in range(m):
            if not flag:
                if board[i][j]=='R':
                    dot=[i,j]
                    flag = True
            tmp.append(False)
        visited.append(tmp)
    
    visited[dot[0]][dot[1]]=True
    
    q=deque()
    q.append([dot[0],dot[1], 0])
    
    row=[1,0,-1,0]
    col=[0,1,0,-1]
    
    while q:
        x,y,cnt = q.popleft()
        if board[x][y]=="G":
            answer=cnt
            break
        
        for i in range(4):
            if 0<=x+col[i]<n and 0<=y+row[i]<m and board[x+col[i]][y+row[i]]!="D":
                j=1
                while True:
                    if 0<=x+col[i]*j<n and 0<=y+row[i]*j<m:
                        if board[x+col[i]*j][y+row[i]*j]=="D":
                            if not visited[x+col[i]*(j-1)][y+row[i]*(j-1)]:
                                q.append([x+col[i]*(j-1), y+row[i]*(j-1), cnt+1])
                                visited[x+col[i]*(j-1)][y+row[i]*(j-1)]=True
                                break
                            else:
                                break
                        else:
                            j+=1
                            continue

                    else:
                        if not visited[x+col[i]*(j-1)][y+row[i]*(j-1)]:
                            q.append([x+col[i]*(j-1), y+row[i]*(j-1), cnt+1])
                            visited[x+col[i]*(j-1)][y+row[i]*(j-1)]=True
                            break
                        else:
                            break
                    
    return answer