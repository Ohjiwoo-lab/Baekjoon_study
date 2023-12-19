from collections import deque

def bfs(visited, dot, x, y):
    row = [1,0,-1,0]
    col = [0,1,0,-1]
    
    cnt=0
    q=deque()
    q.append(dot)
    cnt+=int(visited[dot[0]][dot[1]])
    visited[dot[0]][dot[1]] = "X"
    
    while q:
        nDot = q.popleft()
        for i in range(4):
            if 0 <= (nDot[0]+col[i]) < y and 0 <= (nDot[1]+row[i]) < x and visited[nDot[0]+col[i]][nDot[1]+row[i]] != "X":
                cnt += int(visited[nDot[0]+col[i]][nDot[1]+row[i]])
                visited[nDot[0]+col[i]][nDot[1]+row[i]] = "X"
                q.append([nDot[0]+col[i], nDot[1]+row[i]])
    
    return cnt
    
def solution(maps):
    answer = []
    
    x = len(maps[0])
    y = len(maps)

    visited=[]
    for i in maps:
        tmp=[]
        for j in i:
            tmp.append(j)
        visited.append(tmp)

    for i in range(y):
        for j in range(x):
            if visited[i][j] != "X":
                answer.append(bfs(visited, [i,j], x, y))
    
    if len(answer)==0:
        answer.append(-1)
    else:
        answer.sort()
    
    return answer